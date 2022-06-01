from pickle import NONE
from  src.binaryconvert import ConvertiInBinario
import unittest


def test_binary () -> None:
    assert ConvertiInBinario(4) == '100 '
    return True
    #assert ConvertiInBinario(8) == "1000"