# test python utilities
import pytest
import pandas as pd

from python.utils import load_data_file

TEST_DATA_PATH = "tests/test_data"


def test_load_data_file_csv():
    data = load_data_file(filepath=f"{TEST_DATA_PATH}/compare_data_a.csv")
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 3


def test_load_data_file_json():
    data = load_data_file(filepath=f"{TEST_DATA_PATH}/compare_data_a.json")
    assert isinstance(data, pd.DataFrame)
    assert len(data) == 2

def test_load_data_file_other():
    with pytest.raises(NotImplementedError):
        load_data_file(filepath=f"{TEST_DATA_PATH}/data_file.parquet")
