from random import randint

def roll_dice() -> int:
    return randint(1, 6)

def simulate_risk_fight() -> bool:
    red = sorted([roll_dice() for i in range(3)])
    blue = sorted([roll_dice() for i in range(3)])
    print(red)
    print(blue)

    B_points = 0;
    R_points = 0;
    
    for i in range(len(red)):
        if red[i] <= blue[i]:
            B_points += 1
        else:
            R_points += 1

    if R_points > B_points:
        return True
    
    return False

if __name__ == "__main__":
    if simulate_risk_fight():
        print("Ha vinto il rosso!!")
    else:
        print("Ha vinto il blue!!")