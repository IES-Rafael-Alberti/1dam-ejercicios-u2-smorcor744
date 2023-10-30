import pytest
from src.ej5_02 import datos, siono

@pytest.mark.parametrize(
    "input_n, input_m, expected",
    [
        (4, 7, False),
        (1000, 10, False),
        (16, 1000, False),
        (17, 1000, True),
        (50, 500, False),
        (45, 12444, True)
    ]
)
def test_siono_params(input_n, input_m, expected):
    assert siono(input_n, input_m) == expected