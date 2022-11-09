if __name__ == "__main__":

    data = {"BarackObama":"44th president of the United States", "SandroPertini":"Former President of the Italian Republic", "NelsonMandela":"Former President of South Africa", "MahatmaGandhi":"Bapu", "DonaldKnuth":"Creator of LaTeX", "DennisRitchie":"Creator of C"}
    value = input("Enter a famous name+surname, ex. BarackObama: ")

    if value in data:
        print(f'Result: "{data[value]}".')
    else:
        print('Invalid input! Please enter a good name!')
    