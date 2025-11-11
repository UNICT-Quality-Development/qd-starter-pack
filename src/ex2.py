def insert_week_number() -> int:
    while True:
        print("insert week number")
        n_string = input().strip()
        if not n_string:
            print("Invalid input! Please enter week number between 1-7")
        elif n_string.isdigit() and 1 <= int(n_string) <= 7:
            return int(n_string)
        else:
            print("Invalid input! Please enter week number between 1-7")

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
n_day = insert_week_number()
print(week_days[n_day - 1])