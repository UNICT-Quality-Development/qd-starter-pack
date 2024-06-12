from src.binary_converter import binary_converter
import pytest


@pytest.fixture
def mocker():
    from unittest.mock import Mock

    return Mock()


@pytest.fixture
def binary_converter_function():
    return binary_converter


def test_binary_converter_positive_integer(binary_converter_function):
    decimal_number = 10
    binary_result = binary_converter_function(decimal_number)
    assert binary_result == "1010"


def test_binary_converter_zero(binary_converter_function):
    decimal_number = 0
    binary_result = binary_converter_function(decimal_number)
    assert binary_result == "0"


def test_binary_converter_negative_integer(binary_converter_function):
    decimal_number = -5
    with pytest.raises(ValueError):
        binary_converter_function(decimal_number)


def test_binary_converter_large_integer(binary_converter_function):
    decimal_number = 1234567890
    binary_result = binary_converter_function(decimal_number)
    assert binary_result == "1001001100101100000001011010010"
