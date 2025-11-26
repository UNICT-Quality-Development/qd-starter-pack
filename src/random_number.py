#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
import random
import sys


def random_positive_int() -> int:
    return random.randint(0, sys.maxsize)


# maybe limited_random... is a better name?
def random_limited_positive_int(upper_limit):
    try:
        assert isinstance(upper_limit, int)
    except:
        raise Exception("use integers only")
    try:
        assert upper_limit > 0 and upper_limit <= sys.maxsize
    except:
        raise Exception("Sorry, no numbers below or equal to zero")
    return random.randint(0, upper_limit)


def main():
    print(random_positive_int())

    user_input = None
    while user_input is None:
        try:
            user_input = int(
                input(
                    "Inserisci un limite superiore INTERO e POSITIVO per il range di generazione: "
                )
            )
            print(random_limited_positive_int(user_input))
        except:
            print("Errore: tipo o valore del limite superiore non validi")
            user_input = None


if __name__ == "__main__":
    main()
