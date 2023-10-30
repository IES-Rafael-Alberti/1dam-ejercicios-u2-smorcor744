import pytest
from src.ej6_02 import datos, grupoA

@pytest.mark.parametrize(
    "input_n, input_m, expected",
    [
        ("maria", "hOMBRE", False),
        ("Maria Jose", "Mujer", True),
        ("Jose Maria", "mujer", False),
        ("X","mujer", False),
    ]
)
def test_grupoA_params(input_n, input_m, expected):
    assert grupoA(input_n, input_m) == expected
