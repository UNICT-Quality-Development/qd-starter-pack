from src.ex4 import days_of_month
import pytest

arr31 = [1,3,5,7,8,12]
arr30 = [4,6,9,11]

def test_days_of_month() -> None:
    for i in range(len(arr31)):
        assert days_of_month(arr31[i]) == "31"

    for i in range(len(arr30)):
        assert days_of_month(arr30[i]) == "30"

    assert days_of_month(2) == "28/29"
    
    with pytest.raises(SystemExit) as e:
        days_of_month(15)

    assert e.type == SystemExit
