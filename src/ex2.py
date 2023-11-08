
giorniDellaSettimana = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def func(a:int)->None:
    match a:
        case 1:
             z = giorniDellaSettimana[0]
        case 2:
             z = giorniDellaSettimana[1]
        case 3:
             z = giorniDellaSettimana[2]
        case 4:
             z = giorniDellaSettimana[3]
        case 5:
             z = giorniDellaSettimana[4]
        case 6:
             z = giorniDellaSettimana[5]
        case 7:
             z = giorniDellaSettimana[6]
        case _:
             z = "numero inserito errato"
    return z
