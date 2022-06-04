from random import randint

def get_random_number(max_value: int = 2147483647) -> int:
    return randint(0, max_value)