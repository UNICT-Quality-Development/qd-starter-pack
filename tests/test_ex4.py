from src.ex4 import ex4

def test_ex4() -> None:
    assert ex4(0) == "Invalid input! Please enter month number between 1-12"
    assert ex4(1) == "31 days"
    assert ex4(2) == "28/29 days"
    assert ex4(3) == "31 days"
    assert ex4(4) == "30 days"
    assert ex4(5) == "31 days"
    assert ex4(6) == "30 days"
    assert ex4(7) == "31 days"
    assert ex4(8) == "31 days"
    assert ex4(9) == "30 days"
    assert ex4(10) == "31 days"
    assert ex4(11) == "30 days"
    assert ex4(12) == "31 days"
    for i in range(13,100):
        assert ex4(i) == "Invalid input! Please enter month number between 1-12"
