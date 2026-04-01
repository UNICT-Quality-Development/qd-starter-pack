# What about implementhing this using "match" ?
#
# #include <iostream>
# using namespace std;
#
# int main()
# {
#   string textInput;
#
#   cout << "Enter a famous name+surname, ex. BarackObama " << endl;
#   cin >> textInput;
#
#   if (textInput == "BarackObama")
#   {
#     cout << "44th president of the United States" << endl;
#   }
#   else if (textInput == "SandroPertini")
#   {
#     cout << "Former President of the Italian Republic" << endl;
#   }
#   else if (textInput == "NelsonMandela")
#   {
#     cout << "Former President of South Africa" << endl;
#   }
#   else if (textInput == "MahatmaGandhi")
#   {
#     cout << "Bapu" << endl;
#   }
#   else if (textInput == "DonaldKnuth")
#   {
#     cout << "Creator of LaTeX" << endl;
#   }
#   else if (textInput == "DennisRitchie")
#   {
#     cout << "Creator of C" << endl;
#   }
#   else
#   {
#     cout << "Invalid input! Please enter a good name!" << endl;
#   }
#
#   return 0;
# }

# Input del nome e cognome famoso
nome = input("Inserisci un nome e cognome famoso, es. BarackObama: ")

# Match per controllare il nome e stampare la descrizione
match nome:
    case "BarackObama":
        print("44° presidente degli Stati Uniti")
    case "SandroPertini":
        print("Ex Presidente della Repubblica Italiana")
    case "NelsonMandela":
        print("Ex Presidente del Sudafrica")
    case "MahatmaGandhi":
        print("Bapu")
    case "DonaldKnuth":
        print("Creatore di LaTeX")
    case "DennisRitchie":
        print("Creatore del linguaggio C")
    case _:
        print("Input non valido! Inserisci un nome corretto!")
