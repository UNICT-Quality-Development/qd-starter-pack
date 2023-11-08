import pytest
import random 
from unittest.mock import patch
from src.random_1 import rand

def test_numero_5():
    # Imposta un valore fisso per il random.randint
    with patch.object(random, 'randint', return_value=5):
        numero_casuale = rand()
    
    assert numero_casuale == 5

def test_numero_10():
    # Imposta un valore fisso per il random.randint
    with patch.object(random, 'randint', return_value=10):
        numero_casuale = rand()
    
    assert numero_casuale == 10

def test_random_ce():
    assert 1 <= rand() <= 10