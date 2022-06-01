#Surprise!
def ex4(month : int) -> str:
    month_len = ""
    match month:
        case 1:
            month_len = "31 days"
        case 2:
            month_len = "28/29 days"
        case 3:
            month_len = "31 days"
        case 4:
            month_len = "30 days"
        case 5:
            month_len = "31 days"
        case 6:
            month_len = "30 days"
        case 7:
            month_len = "31 days"
        case 8:
            month_len = "31 days"
        case 9:
            month_len = "30 days"
        case 10:
            month_len = "31 days"
        case 11:
            month_len = "30 days"
        case 12:
            month_len = "31 days"
        case _:
            month_len = "Invalid input! Please enter month number between 1-12"
    print(month_len)
    return month_len
