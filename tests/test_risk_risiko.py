from src.risk_risiko import check_attack


def test_check_attack() -> None:
    red_dices = [6, 5, 4]
    blue_dices = [3, 2, 1]

    result = check_attack(red_dices, blue_dices)
    assert result is 0
    assert result is not None
