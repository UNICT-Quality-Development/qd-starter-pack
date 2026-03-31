from typing import List
import pytest
from src import calculator


parametri: List[dict] = [
    {"a": 1, "b": 2, "ris_addiz": 3, "ris_sottr": -1, "ris_molti": 2, "ris_divis": 0.5},
    {
        "a": -1,
        "b": 1,
        "ris_addiz": 0,
        "ris_sottr": -2,
        "ris_molti": -1,
        "ris_divis": -1,
    },
    {
        "a": -1,
        "b": -2,
        "ris_addiz": -3,
        "ris_sottr": 1,
        "ris_molti": 2,
        "ris_divis": 0.5,
    },
    {"a": 0, "b": 5, "ris_addiz": 5, "ris_sottr": -5, "ris_molti": 0, "ris_divis": 0},
    {
        "a": 0,
        "b": 0,
        "ris_addiz": 0,
        "ris_sottr": 0,
        "ris_molti": 0,
        "ris_divis": "incalcolabile. Divisione per zero non consentita.",
    },
    {
        "a": 1000,
        "b": 999,
        "ris_addiz": 1999,
        "ris_sottr": 1,
        "ris_molti": 999000,
        "ris_divis": 1.001001001,
    },
    {
        "a": 1.5,
        "b": 2.5,
        "ris_addiz": 4.0,
        "ris_sottr": -1,
        "ris_molti": 3.75,
        "ris_divis": 0.6,
    },
    {
        "a": -1.0,
        "b": 1.0,
        "ris_addiz": 0.0,
        "ris_sottr": -2.0,
        "ris_molti": -1.0,
        "ris_divis": -1.0,
    },
    {
        "a": 0.1,
        "b": 0.2,
        "ris_addiz": 0.3,
        "ris_sottr": -0.1,
        "ris_molti": 0.02,
        "ris_divis": 0.5,
    },
    {
        "a": 5,
        "b": 0.5,
        "ris_addiz": 5.5,
        "ris_sottr": 4.5,
        "ris_molti": 2.5,
        "ris_divis": 10.0,
    },
]


@pytest.mark.parametrize("test", parametri)
def test_addizione(test: dict) -> float:
    ris_attuale = calculator.addizione(test["a"], test["b"])
    assert test["ris_addiz"] == pytest.approx(ris_attuale)


@pytest.mark.parametrize("test", parametri)
def test_sottrazione(test: dict) -> float:
    ris_attuale = calculator.sottrazione(test["a"], test["b"])
    assert test["ris_sottr"] == pytest.approx(ris_attuale)


@pytest.mark.parametrize("test", parametri)
def test_moltiplicazione(test: dict) -> float:
    ris_attuale = calculator.moltiplicazione(test["a"], test["b"])
    assert test["ris_molti"] == pytest.approx(ris_attuale)


@pytest.mark.parametrize("test", parametri)
def test_divisione(test: dict) -> float:
    ris_attuale = calculator.divisione(test["a"], test["b"])
    assert test["ris_divis"] == pytest.approx(ris_attuale)


@pytest.mark.parametrize("test", parametri)
def test_input(mocker, test: dict):
    mocker.patch("builtins.input", side_effect=[float(test["a"]), float(test["b"])])
    a, b = calculator.prendi_input()
    assert a == test["a"]
    assert b == test["b"]
