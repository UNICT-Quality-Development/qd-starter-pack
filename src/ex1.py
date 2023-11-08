def get_week_day (week: int) -> str:

    if week < 1 or week > 7:
        return None
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return days[week - 1]
