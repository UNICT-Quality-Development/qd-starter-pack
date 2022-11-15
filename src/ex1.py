#Improve this program using a switch-case. 
def match_days(x: int) -> str: 
    match week: 
        case 1:
            return print("It's Monday")
        case 2:
            return print("It's Tuesday")
        case 3:
            return print("It's Wednesday")
        case 4:
            return print("It's Thursday")
        case 5:
            return print("It's Friday")
        case 6:
            return print("It's Saturday")
        case 7:
            return print("It's Sunday")
        case default:
            return print("There isn't any day with this number.")

if __name__=='__main__':

    week=int(input("Insert a number from 1 to 7: "))
    match_days(week)





    

   
