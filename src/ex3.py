def func(k:str):
    match k:
        case "BarackObama":
            z = "44th president of the United States"
        case "SandroPertini":
            z = "Former President of the Italian Republic"
        case "NelsonMandela":
            z = "Former President of South Africa"
        case "MathmaGandi":
            z = "Bapu"
        case "DonaldKnuthu":
            z = "Creator of Latex"
        case "DenniesRitchu":
            z = "Creator of C"
        case _:
            z = "Inavlid input"
    return z
