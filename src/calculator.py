#
#   Write a program that given two numbers as input make the main operations.
#
#   Output:
#   Insert first number: 4
#   Insert second number: 2
#
#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2
#


print("Insert first number:")
n1 = input()
print("Insert second number:")
n2 = input()

def func(n1,n2):
    risultati = []
    risultati.append(int(n1)+int(n2))
    risultati.append(int(n1)-int(n2))
    risultati.append(int(n1)*int(n2))
    risultati.append(int(n1)/int(n2))

    return risultati

phrases = ["Sum:","Difference:", "Multiplication:", "Division:"]

results = func(n1,n2)
for i in range(4):
    print(phrases[i] + str(results[i]))
