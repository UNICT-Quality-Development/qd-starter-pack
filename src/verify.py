array = [2,4,6,8,10,12,14,16,18,20]

def verify(number : int) -> bool:
    if number in array:
        print("Numero presente")
        return True
    else:
        print("Numero non presente")
        return False

if __name__ == "__main__":
    number = int(input("Inserisci numero: "))
    verify(number)