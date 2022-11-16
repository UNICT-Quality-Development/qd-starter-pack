import random

def generate() -> int:
    return random.randint(1,10)

def main():
    print("The random number is:", generate())

if __name__ == "__main__":
    main()
