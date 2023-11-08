import sys
import pytest
import pytest_mock
sys.path.append("../src")
from binary_converter import print_binary_number
import binary_converter

def test_binary(mocker):
	spy = mocker.spy(binary_converter, "print_binary_number")
	print_binary_number(8)
	assert spy.call_count == 4-1

def test_binary2(mocker):
	spy = mocker.spy(binary_converter, "print_binary_number")
	print_binary_number(16)
	assert spy.call_count == 5-1
	