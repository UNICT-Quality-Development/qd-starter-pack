days = ["Invalid input! Please enter week number between 1-7.", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_day(num_of_day: int) -> str:
    if num_of_day >= 1 and num_of_day <= 7:
        return days[num_of_day]
    else:
        return days[0]