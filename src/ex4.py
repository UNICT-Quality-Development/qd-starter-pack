#Surprise!
def ex4(month : int) -> str:
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return "31 days"
        case 2:
            return "28/29 days"
        case 4 | 6 | 9 | 11:
            return "30 days"
        case _:
            return "Invalid input! Please enter month number between 1-12"
     
