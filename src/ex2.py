


giorniDellaSettimana = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def func(a:int)->int:
    match a:
        case 1:
            print(giorniDellaSettimana[0])
        case 2:
            print(giorniDellaSettimana[1])
        case 3:
            print(giorniDellaSettimana[2])
        case 4:
            print(giorniDellaSettimana[3])
        case 5:
            print(giorniDellaSettimana[4])
        case 6:
            print(giorniDellaSettimana[5])
        case 7:
            print(giorniDellaSettimana[6])
        case _:
            print("numero inserito errato")
        

print("inserisci numero da 1 a 7:")
k = int(input())
func(k)
