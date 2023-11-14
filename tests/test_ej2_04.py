import pytest
from src.ej4_02 import numero, par_impar

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (4, True),
        (0, True),
        (5, False),
        (52521, False)
        (7, False),
        (8, True)
    ]
)
def test_par_impar_params(input_n, expected):
    assert par_impar(input_n) == expected