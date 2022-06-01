"""
Write a program that given two numbers as input make the main operations.

  Output:
  Insert first number: 4
  Insert second number: 2

  SUM: 6
  Difference: 2
  Multiplication: 8
  Division: 2
"""

def Calculator(n1, n2):
    return n1+n2,n1-n2,n1*n2,int(n1/n2)

if __name__ == "__main__":
    l = ("SUM", "Difference", "Multiplication", "Division")
    c = Calculator(int(input("Insert first number: ")),int(input("Insert second ")))
    for i in range(4):
        print(l[i]+":", c[i])
