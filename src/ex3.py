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


def get_description(name):
    match name:
        case "BarackObama":
            return "44th president of the United States"
        case "SandroPertini":
            return "Former President of the Italian Republic"
        case "NelsonMandela":
            return "Former President of South Africa"
        case "MahatmaGandhi":
            return "Bapu"
        case "DonaldKnuth":
            return "Creator of LaTeX"
        case "DennisRitchie":
            return "Creator of C"
        case "LautaroMartinez":
            return "Il mio capitano"
        case _:
            return "Invalid input! Please enter a good name!"


if __name__ == "__main__":
    text_input = input("Enter a famous name+surname, ex. BarackObama\n")
    print(get_description(text_input))
