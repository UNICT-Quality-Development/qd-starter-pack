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


def get_description(name: str) -> str:
    match name:
        case "BarackObama":
            description = "44th president of the United States"
        case "SandroPertini":
            description = "Former President of the Italian Republic"
        case "NelsonMandela":
            description = "Former President of South Africa"
        case "MahatmaGandhi":
            description = "Bapu"
        case "DonaldKnuth":
            description = "Creator of LaTeX"
        case "DennisRitchie":
            description = "Creator of C"
        case "LautaroMartinez":
            description = "Il mio capitano"
        case _:
            description = "Invalid input! Please enter a good name!"

    return description


if __name__ == "__main__":
    text_input = input("Enter a famous name+surname, ex. BarackObama\n")
    print(get_description(text_input))
