name_and_surname = input('Enter a famous name+surname, ex. BarackObama: ')

description = {'BarackObama':'44th President of the United States','SandroPertini': 'Former President of the Italian Republic', 'NelsonMandela':'Former President of South Africa','MahatmaGandhi':'Bapu','DonaldKnuth':'Creator of LaTeX','DenisRitchie':'Creatore of C'}

if name_and_surname in description:
    print(description[name_and_surname])
else:
    print('Invalid input! Please enter a good name!')
