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
    #raises a ValueError on failure
    assert isinstance(upper_limit, int)
    try:
        assert upper_limit > 0 and upper_limit <= sys.maxsize
    except AssertionError as e:
        raise ValueError("input a positive non-zero number") from e
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
        except KeyboardInterrupt:
            print(" ")
            sys.exit(1)
        except Exception as e:
            print(e)
            user_input = None


if __name__ == "__main__":
    main()
