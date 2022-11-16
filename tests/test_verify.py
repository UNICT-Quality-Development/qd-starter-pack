from src.verify import verify

def test_verify() -> None:
	assert verify([3,5,8], 5) == True
	assert verify([3,5,8], 12) == False
	assert verify([2,6,0], 7) == False
	assert verify([2,6,0], 6) == True