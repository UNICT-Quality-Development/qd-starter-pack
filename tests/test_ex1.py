from src.ex1 import main
import builtins

data = [
    (1, "Monday\n"),
    (2, "Tuesday\n"),
    (3, "Wednesday\n"),
    (4, "Thursday\n"),
    (5, "Friday\n"),
    (6, "Saturday\n"),
    (7, "Sunday\n"),
    (8, "Invalid input! Please enter week number between 1-7.\n"),
    (0, "Invalid input! Please enter week number between 1-7.\n"),
    (-1, "Invalid input! Please enter week number between 1-7.\n"),
    ("abc", "Invalid input! Please enter a valid integer between 1-7.\n"),
]


def test_main(monkeypatch, capsys):
    for week_input, expected_output in data:
        monkeypatch.setattr(builtins, "input", lambda _: str(week_input))

        main()

        captured = capsys.readouterr()
        assert expected_output == captured.out
