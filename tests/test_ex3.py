"""Unit tests for src.ex3."""

import pytest

from src.ex3 import get_famous_person

TEST_CASES = [
    ("BarackObama", "44th president of the United States"),
    ("SandroPertini", "Former President of the Italian Republic"),
    ("NelsonMandela", "Former President of South Africa"),
    ("MahatmaGandhi", "Bapu"),
    ("DonaldKnuth", "Creator of LaTeX"),
    ("DennisRitchie", "Creator of C"),
    ("UnknownPerson", "Invalid input! Please enter a good name!"),
]


@pytest.mark.parametrize("name,expected_description", TEST_CASES)
def test_get_famous_person(name: str, expected_description: str) -> None:
    assert get_famous_person(name) == expected_description
