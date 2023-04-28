# test boilerplate approaches used in other test files
import pytest

# ensure imports or project modules work
from python.utils import load_data_file


def test_always_passes():
    assert True


@pytest.mark.skip(reason="skipping failing test")
def test_skip_failing_test():
    assert False


@pytest.mark.xfail(reason="test expected fail")
def test_expect_failing_test():
    assert False


@pytest.mark.parametrize("test_input", [0, 1])
def test_parametrize_input(test_input):
    assert test_input >= 0


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (0, 0),
        (1, 2),
    ],
)
def test_parametrize_input_expected(test_input, expected):
    assert test_input * 2 == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("3 + 5", 8),
        ("2 + 4", 6),
        pytest.param(
            "6 * 9",
            42,
            marks=pytest.mark.xfail,
            id="test_input param expected to fail",
        ),
    ],
)
def test_parametrize_complex(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_parametrize_all_combinations(x, y):
    pass


@pytest.mark.slow_test()
def test_slow_test():
    assert True
