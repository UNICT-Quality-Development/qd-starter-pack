
"""if(int(week) == 1):
    print("Monday")
elif(int(week) == 2):
    print("Tuesday")
elif(int(week) == 3):
    print("Wednesday")
elif(int(week) == 4):
    print("Thursday")
elif(int(week) == 5):
    print("Friday")
elif(int(week) == 6):
    print("Saturday")
elif(int(week) == 7):
    print("Sunday")
else:
    print("Wrong number")"""

def days(week) -> str:
    match int(week):
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Wrong number"