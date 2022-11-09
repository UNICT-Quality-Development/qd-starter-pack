import random

def random_number() -> int:
    return random.randint(1,1000000)

if __name__ == "__main__":
    print("The random number is: ", random_number())
