from main import main_sum
from src.check import sum2

def test_main_sum() -> None:
    assert main_sum(3,4) == 7
    assert sum2(3,4) == 7
