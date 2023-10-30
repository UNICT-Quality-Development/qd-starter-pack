def func()->None:
    print("Enter month number(1-12):")

    k = int(input())
    match k:
        case 1:
            print("31 days")
        case 2:
            print("28/29 days")
        case 3:
            print("31 days")
        case 4:
            print("30 days")
        case 5:
            print("31 days")
        case 6:
            print("30 days")
        case 7:
            print("31 days")
        case 8:
            print("31 days")
        case 9:
            print("30 days")
        case 10:
            print("31 days")
        case 11:
            print("30 days")
        case 12:
            print("31 days")
        case _:
            print("error ")

func()
