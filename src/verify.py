array = [2,4,6,8,10,12,14,16,18,20]

def is_element_in_list(number : int) -> bool:
    if number in array:
        print("Numero presente")
        return True
    
    print("Numero non presente")
    return False

if __name__ == "__main__":
    n = int(input("Inserisci numero: "))
    is_element_in_list(n)
