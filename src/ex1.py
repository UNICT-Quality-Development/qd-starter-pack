def get_week_day (week: int) -> int:

    day = ""

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

    return day