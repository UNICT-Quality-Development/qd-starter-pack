def is_num_present(num_to_check: int | float) -> bool:
    list_of_num = [1, 5, 13.7, 89, 90, 10, 11]
    if(num_to_check in list_of_num):
        return True
    else:
        return False

def print_check(check: int | float) -> None:
    if is_num_present(check) == True:
        print("The number is present")
    else:
        print("The number is not present")

if __name__ == "__main__":
    print_check(14) 
    print_check(25)
    print_check(89)