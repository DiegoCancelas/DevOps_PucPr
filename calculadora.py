import pytest
from calculadora import somar, dividir

def test_somar():
    assert somar(2, 3) == 5

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(1, 0)
