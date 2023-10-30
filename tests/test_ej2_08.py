import pytest
from src.ej8_02 import main

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (0.0, "Inaceptable: 0€"),
        (0.4, "Aceptable: 960€"),
        (0.6, "Meritorio: 1440€"),
        (0.7876, "Meritorio: 1890.24€"),
        (0.2, "error"),
        (0.5, "error")
    ]
)
def test_main_params(input_n, expected):
    assert main(input_n) == expected