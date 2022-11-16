def get_week_day(week_input):
    switch = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    return switch.get(week_input, "Invalid number!")

if __name__ == "__main__":
    week_input = int(input("Insert a number: "))
    print(f'Day selected: {get_week_day(week_input)}')