# test python utilities
import pytest
import pandas as pd
import geopandas as gpd

from python.utils import (
    load_data_file,
    load_shapefile,
    load_geodata_url,
    convert_to_geodata,
    reporject_geometry,
    WKT_PROJECTION,
    NYC_PROJECTION,
)

TEST_DATA_PATH = "tests/test_data"


def test_load_data_file_csv():
    data = load_data_file(filepath=f"{TEST_DATA_PATH}/minimal_data.csv")
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 3
    assert data["column_b"][2] == "b_2"


def test_load_data_file_json():
    data = load_data_file(filepath=f"{TEST_DATA_PATH}/minimal_data.json")
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 2
    assert data.iloc[1]["key_int"] == 300


def test_load_data_file_not_implemented():
    with pytest.raises(NotImplementedError):
        load_data_file(filepath=f"{TEST_DATA_PATH}/data_file.parquet")


def test_load_shapefile():
    data = load_shapefile(filepath=f"{TEST_DATA_PATH}/Open Streets Locations.zip")
    assert isinstance(data, gpd.GeoDataFrame)
    assert len(data) == 325


def test_load_geodata_url():
    data = load_geodata_url("https://data.cityofnewyork.us/resource/uiay-nctu.geojson")
    assert isinstance(data, gpd.GeoDataFrame)
    assert len(data) == 325


@pytest.mark.skip(reason="result is 'Killed' due to large file")
def test_load_shapefile_large():
    geography = load_shapefile("./.data/dev_db", "housing.shp.zip")
    assert len(geography) > 1


def test_convert_to_geodata():
    data = load_data_file(filepath=f"{TEST_DATA_PATH}/census_counties_nyc.csv")
    data = convert_to_geodata(data)
    assert isinstance(data, gpd.GeoDataFrame)
    assert data.crs == WKT_PROJECTION


def test_reporject_geometry():
    data = load_data_file(filepath=f"{TEST_DATA_PATH}/census_counties_nyc.csv")
    data = convert_to_geodata(data)
    data = reporject_geometry(data, WKT_PROJECTION, NYC_PROJECTION)
    assert data.crs == NYC_PROJECTION
