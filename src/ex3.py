#  Could you still use a switch case here? May you can use a map. 

def is_in_list(name_list: dict, name: str) -> bool:
  return name in name_list

if __name__ == '__main__':
  textInput = input("Enter a famous name+surname, ex. BarackObama ")

  names = { "BarackObama":"44th president of the United States", 
            "SandroPertini": "Former President of the Italian Republic", 
            "NelsonMandela": "Former President of South Africa", 
            "MahatmaGandhi": "Bapu", 
            "DonaldKnuth": "Creator of LaTeX", 
            "DennisRitchie": "Creator of C"
          }

  if ( is_in_list(names, textInput) ):
    print(names[textInput])
  else:
    print("Invalid input! Please enter a good name!")

  