from src.ex1 import get_day


def test_get_day() -> None:
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday", "Invalid input!"]
    for i in (range(len(days))):
        assert get_day(i+1) == days[i]
