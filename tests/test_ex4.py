from src.ex4 import ex4

def test_ex4() -> None:
    expected_results = ["Invalid input! Please enter month number between 1-12", "31 days", "28/29 days", "31 days", "30 days", "31 days", "30 days", "31 days", "31 days", "30 days", "31 days", "30 days", "31 days"]
    for i in range(0,13):
        assert ex4(i) == expected_results[i]
    for i in range(13,100):
        assert ex4(i) == expected_results[0]
