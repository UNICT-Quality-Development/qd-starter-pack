# N = int(input("inserisci un numero: "))


def convert(N):
    MAX_BITS = 32

    j = MAX_BITS - 1

    bits = [0] * MAX_BITS

    while N > 0:
        bits[j] = N % 2
        N = N // 2
        j -= 1
    return "".join([str(x) for x in bits])

print(convert(10))
