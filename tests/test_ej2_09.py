import pytest
from src.ej9_02 import main

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (3, "Gratis"),
        (4, "5€"),
        (19, "10€"),
        (23, "10€"),
        ("", "error"),
    ]
)
def test_main_params(input_n, expected):
    assert main(input_n) == expected