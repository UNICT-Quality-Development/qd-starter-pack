import src.calculator
import pytest
import random


@pytest.fixture
def mocker():
    from unittest.mock import Mock

    return Mock()


@pytest.fixture
def fun_sum():
    return src.calculator.sum


@pytest.fixture
def fun_sub():
    return src.calculator.sub


@pytest.fixture
def fun_mul():
    return src.calculator.mul


@pytest.fixture
def fun_div():
    return src.calculator.div


def fun_mod():
    return src.calculator.mod


def test_sum_positive_integers(fun_sum):
    result = fun_sum(5, 3)
    assert result == 8


def test_sum_negative_integers(fun_sum):
    result = fun_sum(-10, 5)
    assert result == -5


def test_sum_mixed_signs(fun_sum):
    result = fun_sum(-7, 3)
    assert result == -4


def test_sum_large_numbers(fun_sum):
    result = fun_sum(1000000, 9999999)
    assert result == 10999999


def test_sum_zero(fun_sum):
    result = fun_sum(0, 0)
    assert result == 0


def test_sum_identity_property(fun_sum):
    for i in range(-100, 100):
        assert fun_sum(i, 0) == i
        assert fun_sum(0, i) == i


def test_sub_positive_integers(fun_sub):
    result = fun_sub(5, 3)
    assert result == 2


def test_sub_negative_integers(fun_sub):
    result = fun_sub(-10, -5)
    assert result == -5


def test_sub_mixed_signs(fun_sub):
    result = fun_sub(-7, 3)
    assert result == -10


def test_sub_large_numbers(fun_sub):
    result = fun_sub(1000000, 9999999)
    assert result == -8999999


def test_sub_zero(fun_sub):
    result = fun_sub(0, 0)
    assert result == 0


def test_sub_identity_property(fun_sub):
    for i in range(-100, 100):
        assert fun_sub(i, 0) == i
        assert fun_sub(0, i) == -i


def test_mul_mixed_signs(fun_mul):
    assert fun_mul(-1, 10) == -10


def test_mul_negative_integers(fun_mul):
    assert fun_mul(-1, -10) == 10


def test_mul_identity_property(fun_mul):
    for i in range(-100, 100):
        assert fun_mul(i, 1) == i
        assert fun_mul(1, i) == i


def test_division_float_result(fun_div):
    operand_a = 7
    operand_b = 2
    assert fun_div(operand_a, operand_b) == 3.5


def test_division_by_zero(fun_div):
    operand_a = random.randint(1, 10)
    operand_b = 0
    with pytest.raises(ZeroDivisionError):
        fun_div(operand_a, operand_b)
