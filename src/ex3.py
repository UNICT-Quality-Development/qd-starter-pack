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


def descriptor():
    text_input = input("Enter a famous name+surname, ex. BarackObama ")

    namesDesc = {
        "BarackObama" : "44th president of the United States",
        "SandroPertini" : "Former President of the Italian Republic",
        "NelsonMandela" : "Former President of South Africa",
        "MahatmaGandhi" : "Bapu",
        "DonaldKnuth" : " Creator of LaTeX",
        "DennisRitchie" : "Creator of C"
    }

    try:
        print(namesDesc[text_input])
    except:
        print("Invalid input! Please enter a good name!")

descriptor()