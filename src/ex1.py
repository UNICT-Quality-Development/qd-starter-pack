


def func(a:int)->int:
    match a:
        case 1:
             print("Monday")
        case 2:
             print("Tuesday")
        case 3:
             print("Wednesady")
        case 4:
             print("Thursday")
        case 5:
             print("Friday")
        case 6:
             print("Saturday")
        case 7:
             print("Sunday")
        case _:
             print("numero inserito errato")
        

print("inserisci numero da 1 a 7:")
k = int(input())
func(k)
