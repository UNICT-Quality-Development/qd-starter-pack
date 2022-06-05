def who_is(text:str,dictionary:dict) -> str:    
    if text in dictionary:
        return dictionary[text]
    else:
        return "Invalid input! Please enter a good name!"

def main() -> int: # pragma: no cover
    dictionary = {"BarackObama":"44th president of the United States",
                  "SandroPertini":"Former President of the Italian Republic",
                  "NelsonMandela":"Former President of South Africa",
                  "MahatmaGandhi":"Bapu",
                  "DonaldKnuth":"Creator of LaTeX",
                  "DennisRitchie":"Creator of C"}

    textInput = str(input("Enter a famous name+surname, ex: BarackObama: "))
    print(who_is(textInput,dictionary))
    return 0

if __name__ == "__main__": # pragma: no cover
    main()