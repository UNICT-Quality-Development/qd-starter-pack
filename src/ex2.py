
def day_of_week(n:int) -> str:
    arr = ["ND","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if n >= 1 and n <= 7:
        return arr[n]
    else:
        return "Invalid input! Please enter week number between 1-7."

def main(): # pragma: no cover
    n = int(input("Enter week number(1-7): "))
    print(day_of_week(n))

if __name__ == "__main__": # pragma: no cover
    main()