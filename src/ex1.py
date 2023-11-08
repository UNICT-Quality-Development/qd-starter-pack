def get_week_day (week: int) -> int:

    if week == 1:
        day = "Monday"
    elif week == 2:
        day = "Tuesday"
    elif week == 3:
        day = "Wednesday"
    elif week == 4:
        day = "Thursday"
    elif week == 5:
        day = "Friday"
    elif week == 6:
        day = "Saturday"
    elif week == 7:
        day = "Sunday"
    else:
        print("Invalid input! Please enter week number between 1-7.")
    
    print(day)

    return 0