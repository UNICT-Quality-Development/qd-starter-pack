# Improve this program replacing if/else if with an array.


def day_of_the_week():
    # Input week number from user
    weekDay = int(input("Enter week number(1-7): "))
    daysOfTheWeek = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    if weekDay not in range(1, 8):  # range usa un intervallo [a,b[
        print("Error: number not in expected range (1 through 7), retry.")
    else:
        print(f"Selected day: {daysOfTheWeek[weekDay-1]}")


day_of_the_week()
