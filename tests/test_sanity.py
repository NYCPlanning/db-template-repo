# test boilerplate approaches used in other test files
import pytest

# ensure imports or project modules work
from python.utils import execute_sql_file


def test_always_passes():
    assert True


@pytest.mark.xfail(reason="expected to always fail")
def test_expect_always_fails():
    assert False


@pytest.mark.skip(reason="skipping always fails")
def test_skip_always_fails():
    assert False
