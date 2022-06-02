def convert_to_binary(number: int, bits: int) -> str:
    binary = ''

    for i in range(bits):
        if number > 0:
            binary += str(number % 2)
            number //= 2
        else:
            binary += '0'

    return binary[::-1]