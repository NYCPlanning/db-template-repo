# test python utilities
import pandas as pd
import pytest

from python.utils import load_data_file, load_shapefile

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

@pytest.mark.skip(reason="result is 'Killed' due to large file")
def test_load_shapefile_large():
    geography = load_shapefile("./.data/dev_db", "housing.shp.zip")

    print(type(housing))
    assert len(geography) > 1
