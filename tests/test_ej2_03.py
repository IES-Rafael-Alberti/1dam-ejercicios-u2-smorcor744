import pytest
from src.ej3_02 import numero, division

@pytest.mark.parametrize(
    "input_n, input_m, expected",
    [
        (4, 2, 2),
        (1000, 10, 100),
        (243, 0, "error"),
        (6, 8, 0.75)
    ]
)
def test_division_params(input_n, input_m, expected):
    assert division(input_n, input_m) == expected