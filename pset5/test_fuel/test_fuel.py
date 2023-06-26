import pytest
from fuel import convert, gauge


def test_convert_valid_fraction():
    assert convert("1/2") == 50
    assert convert("3/4") == 75


def test_convert_invalid_fraction():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("2/3.5")


def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(50) == '50%'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
