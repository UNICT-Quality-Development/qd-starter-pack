import random

def randDice() -> int:
    return random.randint(1, 6)

def printDices(dices: list[int]):
    print(dices[0], "(N)")
    print(dices[1], "(M)")
    print(dices[2], "(0)")

def printResults(red: list[int], blue: list[int]):
    print("\n  R    B")
    print("N", red[0], "vs", blue[0], "=>", 'red' if red[0] > blue[0] else 'blue', "wins")
    print("M", red[1], "vs", blue[1], "=>", 'red' if red[1] > blue[1] else 'blue', "wins")
    print("O", red[2], "vs", blue[2], "=>", 'red' if red[2] > blue[2] else 'blue', "wins")

redDices = [randDice(), randDice(), randDice()]
blueDices = [randDice(), randDice(), randDice()]

redDices.sort(reverse = True)
blueDices.sort(reverse = True)

print("\nRed dices:")
printDices(redDices)

print("\nBlue dices:")
printDices(blueDices)

printResults(redDices, blueDices)
