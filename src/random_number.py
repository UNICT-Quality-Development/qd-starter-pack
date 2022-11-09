import random

if __name__ == "__main__":

    value1 = int(input("Insert the range (first value): "))
    value2 = int(input("Insert the range (second value): "))

    if value1 < value2:
        print(f'Random number: {random.randrange(value1, value2, 3)}')
    else:
        print('Invalid range!')
