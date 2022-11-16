
def days_of_week(week_number: str)-> str:
    if int(week_number) >= 1 and int(week_number) <= 7:
        match int(week_number):
            case 1:
                return("Monday")
            case 2:
                return("Tuesday")
            case 3:
                return("Wednesday")
            case 4:
                return("Thursday")
            case 5:
                return("Friday")
            case 6:
                return("Saturday")
            case 7:
                return("Sunday") 
    else:
        return("Invalid input! Please enter week number between 1-7")    