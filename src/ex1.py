def week(i):
    days =[
    "Invalid input! Please enter week number between 1-7.",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
    ]

    if( int(i) < 1 or int(i) > 7 ): 
        index = 0
    else: 
        index = i
    return days[int(index)]

print("Enter week number(1-7): ")
number = input()
print(week(number))
