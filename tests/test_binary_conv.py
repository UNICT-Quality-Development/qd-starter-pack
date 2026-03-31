from typing import List
import pytest
from src import binary_converter

parametri: List[dict] = [
    {"a": 5, "exp_ris": f"{bin(5)[2:]}", "bin_post_carry": list("110")},
    {"a": 1, "exp_ris": f"{bin(1)[2:]}", "bin_post_carry": list("0")},
    {"a": 8, "exp_ris": f"{bin(8)[2:]}", "bin_post_carry": list("1001")},
    {"a": 111, "exp_ris": f"{bin(111)[2:]}", "bin_post_carry": list("1110000")},
    {"a": 2.5, "exp_ris": f"{bin(round(2.5))[2:]}", "bin_post_carry": list("11")},
    {
        "a": 4.0000000,
        "exp_ris": f"{bin(int(4.0000000))[2:]}",
        "bin_post_carry": list("101"),
    },
    {"a": -1, "exp_ris": f"{bin(-1)[3:]}", "bin_post_carry": list("0")},
    {
        "a": 101.0110,
        "exp_ris": f"{bin(int(101.0110))[2:]}",
        "bin_post_carry": list("1100110"),
    },
]

param_invert: List[dict] = [
    {"input": "1", "exp_out": "1111111111111110"},
    {"input": "", "exp_out": "1111111111111111"},
    {"input": "10101010", "exp_out": "1111111101010101"},
    {"input": "1010101010101010", "exp_out": "0101010101010101"},
    {"input": "1111111111111111", "exp_out": "0000000000000000"},
    {"input": "10101010101010101", "exp_out": "01010101010101010"},
]


@pytest.mark.parametrize("test", parametri)
def test_division(test: dict) -> int:
    act_ris = binary_converter.division(int(abs(test["a"])))
    assert test["exp_ris"] == act_ris


@pytest.mark.parametrize("test", parametri)
def test_carry(test: dict) -> str:
    act_ris = binary_converter.carry(test["exp_ris"])
    assert "".join(test["bin_post_carry"]) == act_ris


@pytest.mark.parametrize("test", param_invert)
def test_invert(test: dict) -> str:
    act_ris = binary_converter.invert(test["input"])
    assert test["exp_out"] == act_ris
