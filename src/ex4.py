def days_of_month(m:int) -> str:
    match m:
        case 1 | 3 | 5 | 7 | 8 | 12:
            return "31"
        
        case 4 | 6 | 9 | 11:
            return "30"
        
        case 2:
            return "28/29"
        case _: 
            print("Invalid input! Please enter month number between 1-12")
            exit()             

def main(): # pragma: no cover
    month = int(input("Enter month number(1-12): "))
    print(days_of_month(month),"days")

if __name__ == "__main__": # pragma: no cover
    main()