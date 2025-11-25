#
#   Write a program that given a number as input convert it in binary.
#
#   Output:
#   Insert first number: 8
#   The binary number is: 1000
#


def decimal2binary(n: int) -> str:
    if n < 0:
        raise ValueError("Error - n must be greater than 0")
    res = ""
    while n > 0:
        bit = n & 1
        n = n >> 1
        res = str(bit) + res
    return res


if __name__ == "__main__":  # pragma: no cover
    print(decimal2binary(675))
