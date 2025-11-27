from pytest_mock import MockerFixture 
import src.binary_converter
import pytest
from src import binary_converter

def test_cast() :
    assert binary_converter.cast(0) == ""
    assert binary_converter.cast(3) == "11"

def test_WDPG() :
    assert binary_converter.WDPG(-4.5) == 0

def test_checkValue() :
    assert binary_converter.checkValue("hello") == None

def test_main(mocker) :
    mocker.patch('builtins.input', return_value = '4')
    binary_converter.main()
    
