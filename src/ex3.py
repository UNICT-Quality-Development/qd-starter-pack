text_input = input("Enter a famous name+surname, ex. BarackObama: ")

match text_input:
    case "BarackObama":
        print("44th president of the United States")
    case "SandroPertini":
        print("Former President of the Italian Republic")
    case "NelsonMandela":
        print("Former President of South Africa")
    case "MahatmaGandhi":
        print("Bapu")
    case "DonaldKnuth":
        print("Creator of LaTeX")
    case "DennisRitchie":
        print("Creator of C")
    case _:
        print("Invalid input! Please enter a good name!")
