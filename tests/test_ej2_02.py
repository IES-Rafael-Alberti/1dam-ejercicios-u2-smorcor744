import pytest
from src.ej2_02 import igual, pedircontra

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("contraseña", False),
        ("UsuAriO", True),
        ("USUARIO", True),
        ("", False),
        ("cualquier Palabra", False),
        ("Usuario", True)
    ]
)
def test_igual_params(input_n, expected):
    assert igual(input_n) == expected