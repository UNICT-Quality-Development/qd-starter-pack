from typing import List

import pytest

from src import ex3

tests: List[dict] = [
    {   "input": "BarackObama",     "expected_res": "44th president of the United States",      },
    {   "input": "SandroPertini",   "expected_res": "Former President of the Italian Republic", },
    {   "input": "NelsonMandela",   "expected_res": "Former President of South Africa",         },
    {   "input": "MahatmaGandhi",   "expected_res": "Bapu",                                     },
    {   "input": "DonaldKnuth",     "expected_res": "Creator of LaTeX",                         },
    {   "input": "DennisRitchie",   "expected_res": "Creator of C",                             },
    {   "input": "LautaroMartinez", "expected_res": "Il mio capitano",                          },
    {   "input": "UnknownPerson",   "expected_res": "Invalid input! Please enter a good name!", },
]


@pytest.mark.parametrize("test", tests)
def test_get_description(test: dict) -> None:
    # arrange
    name = test["input"]

    # act
    res = ex3.get_description(name)

    # assert
    assert res == test["expected_res"]
