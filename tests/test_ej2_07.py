import pytest
from src.ej7_02 import datos

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (123, "5"),
        (1000, "15"),
        (19999, "15"),
        (20000, "20"),
        (35000, "30"),
        (61000, "40")
    ]
)
def test_datos_params(input_n, expected):
    assert datos(input_n) == expected
