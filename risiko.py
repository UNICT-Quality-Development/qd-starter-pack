import random
import time

def roll_dice():
    return random.randint(1, 6)

def roll_dices(n, color):
    dices = []
    print(f"\nRolling {n} dices for {color}...")
    for i in range(n):
        val = roll_dice()
        dices.append(val)
        print(f"{color} dice {i+1}: {val}")
        time.sleep(1)  # pausa per simulare l'effetto "lancio"
    dices.sort(reverse=True)
    print(f"{color} dices: {dices}")
    return dices

red_dices = roll_dices(3, "Red")
blue_dices = roll_dices(3, "Blue")
labels = ["N", "M", "O"]

# Confronto dei dadi
print("\n--- Battle Results ---")
print("  R    B")
for label, red, blue in zip(labels, red_dices, blue_dices):
    if red > blue:
        winner = "red wins"
    else:
        winner = "blue wins"
    print(f"{label} {red} vs {blue} => {winner}")