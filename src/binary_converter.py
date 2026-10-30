#
#   Write a program that given a number as input convert it in binary.
#
#   Insert number: 8
#   The binary number is: 1000
#
if __name__ == "__main__":	
	try:
		number= int(input ("Insert number: "))
	except ValueError:
		print ("Ma cosa scrivi! Devi scrivere un intero!")
	if (number<0): 
		exit ("Numeri negativi non ancora supportati! Abbiamo bisogno di personale per programmare funzioni complicate di questo tipo!")
	output=""
	while (number/2>=1):
		# for debugging 
		# print ("n: ",number)
		if (number%2!=0): 
			output+="1"
		else:
			output+="0"
	
		number //=2
	output+=str(number)
	output=output[::-1]
	print ("The binary number is: ", output)	

