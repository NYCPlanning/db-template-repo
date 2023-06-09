# test python utilities
import pandas as pd
import pytest

from python.utils import load_data_file

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

def test_load_data_file_other():
    with pytest.raises(NotImplementedError):
        load_data_file(filepath=f"{TEST_DATA_PATH}/data_file.parquet")