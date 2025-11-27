from src.ex2 import main


data = [
    (1, "Monday\n"),
    (2, "Tuesday\n"),
    (3, "Wednesday\n"),
    (4, "Thursday\n"),
    (5, "Friday\n"),
    (6, "Saturday\n"),
    (7, "Sunday\n"),
    (0, "Invalid input! Please enter week number between 1-7.\n"),
    (8, "Invalid input! Please enter week number between 1-7.\n"),
    (-1, "Invalid input! Please enter week number between 1-7.\n"),
]


def test_main(monkeypatch, capsys):

    for input_value, expected_output in data:
        monkeypatch.setattr("builtins.input", lambda _: str(input_value))
        main()
        captured = capsys.readouterr()
        assert captured.out == expected_output
