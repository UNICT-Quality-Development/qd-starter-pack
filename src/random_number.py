import random

def random_number() -> int:
    return random.randint(1, 100)

if __name__ == "__main__" :
    print(f"The random number is: {random_number()}")
