import random

def generate() -> int:
    return random.randint(1,10)

if __name__ == "__main__":
    print("The random number is:", generate())
