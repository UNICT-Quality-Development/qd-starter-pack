N=[3,4,5,1,2,3,4,9,13,0]

def verify(a):
	for item in N:
		if int(a) == int(item):
			return True
	return False

print("Inserire elemento da cercare:")
x=input()
if verify(x):
	print("L'elemento è nell'array")
else:
	print("L'elemento non è nell'array")