# Improve this program using a switch-case.
def day_of_the_week():
    weekDay = 0
    # Input week number from user
    weekDay = int(input("Enter week number(1-7): "))
    match weekDay:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid input! Please enter week number between 1-7.")


day_of_the_week()
