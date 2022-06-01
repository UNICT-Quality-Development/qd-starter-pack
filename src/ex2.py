def week_list(week) -> str:
    week_days = ("Monday", "Tuesday", "Wednesay", "Thursday", "Friday", "Saturday", "Sunday")

    if week > 7 or week < 1:
        return ""

    return week_days[int(week - 1)]