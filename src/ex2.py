def ex2(n: int) -> str:
	A=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
	if n>=1 and n<8:
		return A[n-1]
	raise Exception("Invalid input. Must be between 1 and 7")
