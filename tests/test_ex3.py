from typing import List

import pytest

from src import ex3

tests: List[dict] = [
    {   "input": "BarackObama",     "res": ex3.get_description, "expected_res": "44th president of the United States",      },
    {   "input": "SandroPertini",   "res": ex3.get_description, "expected_res": "Former President of the Italian Republic", },
    {   "input": "NelsonMandela",   "res": ex3.get_description, "expected_res": "Former President of South Africa",         },
    {   "input": "MahatmaGandhi",   "res": ex3.get_description, "expected_res": "Bapu",                                     },
    {   "input": "DonaldKnuth",     "res": ex3.get_description, "expected_res": "Creator of LaTeX",                         },
    {   "input": "DennisRitchie",   "res": ex3.get_description, "expected_res": "Creator of C",                             },
    {   "input": "LautaroMartinez", "res": ex3.get_description, "expected_res": "Il mio capitano",                          },
    {   "input": "UnknownPerson",   "res": ex3.get_description, "expected_res": "Invalid input! Please enter a good name!", },
]


@pytest.mark.parametrize("test", tests)
def test_get_description(test: dict) -> None:
    # arrange
    name = test["input"]

    # act
    res = test["res"](name)

    # assert
    assert res == test["expected_res"]
    