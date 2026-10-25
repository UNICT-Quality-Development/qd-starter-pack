import pytest

from src.sum import main, sum


def test_sum() -> None:
    assert sum(3, 4) == 7
    assert sum(0, 0) == 0
    assert sum(1, 2) == 3


def test_main_prints_sum_of_two_inputs(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    answers = iter(["3", "5"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(answers))

    main()

    assert capsys.readouterr().out == "SUM: 8\n"
