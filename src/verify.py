def is_num_present(num_to_check: int | float, list_of_num) -> bool:
    return num_to_check in list_of_num

def print_check(check: int | float, list_present) -> None:
    if is_num_present(check, list_present):
        print("The number is present")
    else:
        print("The number is not present")

if __name__ == "__main__":
    num_present = [1.00, 90.00, 14.00, 18.25, 19.15, 89.00]
    print_check(14, num_present)
    print_check(25, num_present)
    print_check(89, num_present)
