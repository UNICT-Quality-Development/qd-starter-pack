
def day_of_week(n:int) -> str:
    match n:
        case 1: 
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid input! Please enter week number between 1-7."

def main(): # pragma: no cover
    n = int(input("Enter week number(1-7): "))
    print(day_of_week(n))
    

if __name__ == "__main__": # pragma: no cover
    main()