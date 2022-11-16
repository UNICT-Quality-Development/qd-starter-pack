from src.ex2 import ex2

def test_ex2() -> None:
	assert ex2(5) == "Thursday"
	assert ex2(2) == "Monday"
	assert ex2(1) == "Sunday"
