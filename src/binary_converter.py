#
#   Write a program that given a number as input convert it in binary.
#
#   Insert number: 8
#   The binary number is: 1000
#
try:
	number= int(input ("Insert number: "))
except ValueError:
	print ("Ma cosa scrivi! Devi scrivere un intero!")
output=""
while (number/2>=1):
	# print ("n: ",number)
	if (number%2!=0): 
		output+="1"
	else:
		output+="0"

	number= number - (int(number/2)) - number%2
output+=str(number)
output=output[::-1]
print ("The binary number is: ", output)	

