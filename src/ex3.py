#Could you still use a switch case here? May you can use a map.


def famous_names(name: str) -> str:
    names : dict = {
        "BarackObama" : "44th president of the United States",
        "SandroPertini" : "Former President of the Italian Republic",
        "NelsonMandela" : "Former President of South Africa",
        "MahatmaGandhi" : "Bapu",
        "DonaldKnuth" : "Creator of LaTeX",
        "DennisRitchie" : "Creator of C",
        "VolodymyrZelensky" : "President of Ukraine"  
    }
    return names[name]
