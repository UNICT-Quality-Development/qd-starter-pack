def func(k:String):
    match k:
        case "BarackObama":
            print("44th president of the United States")
        case "SandroPertini":
            print("Former President of the Italian Republic")
        case "NelsonMandela":
            print("Former President of South Africa")
        case "MathmaGandi":
            print("Bapu")
        case "DonaldKnuthu":
            print("Creator of Latex")
        case "DenniesRitchu":
            print("Creator of C")
        case _:
            print("Inavlid input")

print("Enter a famous name+surname, ex. BarackObama")
k = input()
func(k)