#  Could you still use a switch case here? May you can use a map. 



if __name__ == '__main__':
  textInput = input("Enter a famous name+surname, ex. BarackObama ")

  names = { "BarackObama":"44th president of the United States", 
            "SandroPertini": "Former President of the Italian Republic", 
            "NelsonMandela": "Former President of South Africa", 
            "MahatmaGandhi": "Bapu", 
            "DonaldKnuth": "Creator of LaTeX", 
            "DennisRitchie": "Creator of C"
          }
  if ( textInput in names ):
    print(names[textInput])
  else:
    print("Invalid input! Please enter a good name!")

  