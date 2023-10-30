import random


# Ritorna una lista che contiene 3 interi casuali da 1 a 6
def roll_dice() -> list[int]:
    return [random.randint(1, 6) for _ in range(3)]


# Controlla chi ha vinto, o se c'è stato una pareggio. Ritorna i risultati in una lista di stringhe
def compare_dice(red, blue) -> list[str]:
    result = []
    for r, b in zip(red, blue):
        if r > b:
            result.append("red win")
        elif r < b:
            result.append("blue win")
        else:
            result.append("draw")
    return result


def print_dice(dice: list[int], labels: list[str]):
    # N: first highest number, M: second highest number, O: third highest number
    for i in range(3):
        print(f"{dice[i]} ({labels[i]})")


# Visualizza i risultati, dando in input una lista di dadi rossi, una di dadi blu, e la lista di vittorie / sconfitte / pareggi
def display_results(red, blue, comparison) -> None:
    labels = [
        "N",
        "M",
        "O",
    ]
    print("Red dices:")
    print_dice(red, labels)

    print("\nBlue dices:")
    print_dice(blue, labels)

    print("\n  R    B")
    for i in range(3):
        print(f"{labels[i]} {red[i]} vs {blue[i]} => {comparison[i]}")


# Simula il lancio di dadi per attaccante e difensore
red_dice = roll_dice()
blue_dice = roll_dice()

# Controlla chi ha vinto e visualizza i risultati
comparison_result = compare_dice(red_dice, blue_dice)
display_results(red_dice, blue_dice, comparison_result)
