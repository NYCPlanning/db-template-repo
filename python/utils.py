import os
import pandas as pd
import geopandas as gpd
import contextily as cx
from matplotlib.axes import Axes
from folium.folium import Map
from xyzservices import TileProvider
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

SQL_FILE_DIRECTORY = "sql"
NYC_PROJECTION = "EPSG:2263"
DEFAULT_BASEMAP = cx.providers.Stamen.Terrain
DEFAULT_MAP_CONFIG = {
    "figsize": (10, 10),
    "alpha": 0.5,
    "edgecolor": "g",
    "linewidths": 3,
}


def load_csv_file(directory: str, filename: str) -> pd.DataFrame:
    return pd.read_csv(f"{directory}/{filename}")


def load_shapefile(directory: str, filename: str) -> gpd.GeoDataFrame:
    return gpd.read_file(f"{directory}/{filename}")


def load_geodata_url(url: str) -> gpd.GeoDataFrame:
    return gpd.read_file(url)


def execute_sql_command(command: str) -> None:
    sql_engine = create_engine(os.environ["BUILD_ENGINE"])
    with Session(sql_engine) as session:
        session.execute(text(command))
        session.commit()


def execute_sql_file(filename: str) -> None:
    print(f"Executing {SQL_FILE_DIRECTORY}/{filename} ...")
    sql_file = open(f"{SQL_FILE_DIRECTORY}/{filename}", "r")
    sql_command = ""
    for line in sql_file:
        # ignore comment lines
        if line.strip("\n") and not line.startswith("--"):
            # append line to the command string
            sql_command += line.strip("\n")
            # if the command string ends with ';', it is a full statement
            if sql_command.endswith(";"):
                execute_sql_command(command=sql_command)
                sql_command = ""
            else:
                # continue parsing multi-line statement
                sql_command += " "
        else:
            continue


def query_sql_records(command: str) -> pd.DataFrame:
    sql_engine = create_engine(os.environ["BUILD_ENGINE"])
    with sql_engine.begin() as connection:
        select_records = pd.read_sql(text(command), connection)

    return select_records


def get_source_data_versions() -> pd.DataFrame:
    sql_engine = create_engine(os.environ["BUILD_ENGINE"])
    with sql_engine.begin() as connection:
        select_records = pd.read_sql_table("source_versions", connection)

    return select_records


def pad_map_bounds(
    data: gpd.GeoDataFrame,
    axes: Axes,
    x_scale: float,
    y_scale: float,
) -> Axes:
    lon_min, lat_min, lon_max, lat_max = data.total_bounds
    lon_pad, lat_pad = y_scale * (lon_max - lon_min), x_scale * (lat_max - lat_min)

    axes.axis("scaled")
    axes.axis(
        [lon_min - lon_pad, lon_max + lon_pad, lat_min - lat_pad, lat_max + lat_pad]
    )
    return axes


def map_simple(
    data: gpd.GeoDataFrame,
    projection: str = NYC_PROJECTION,
    basemap: str | TileProvider = DEFAULT_BASEMAP,
    **kwargs,
) -> Axes:
    axes = data.plot(
        **kwargs,
    )
    cx.add_basemap(
        axes,
        crs=projection,
        source=basemap,
    )
    axes.set_axis_off()

    return axes


def map_folium(data: gpd.GeoDataFrame, **kwargs) -> Map:
    # GeoDataFrame.explore fails if any columns have a dtype of object
    for column in data.columns:
        if isinstance(column, object) and column != "geometry":
            data[column] = data[column].astype(str)

    return data.explore(**kwargs)
