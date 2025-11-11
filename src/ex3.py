# What about implementhing this using "match" ?
#
# #include <iostream>
# using namespace std;
#
# int main()
# {
#   string textInput;
#
#   cout << "Enter a famous name+surname, ex. BarackObama ")
#   cin >> textInput;
#
#   if (textInput == "BarackObama")
# #     print(44th president of the United States")
# # if (textInput == "SandroPertini")
# #     print(Former President of the Italian Republic")
# # if (textInput == "NelsonMandela")
# #     print(Former President of South Africa")
# # if (textInput == "MahatmaGandhi")
# #     print(Bapu")
# # if (textInput == "DonaldKnuth")
# #     print(Creator of LaTeX")
# # if (textInput == "DennisRitchie")
# #     print(Creator of C")
# #   else
# #     print(Invalid input! Please enter a good name!")
# #
#   return 0;
# }

good = False
textInput = input("Enter a famous name+surname, ex. BarackObama ")
if textInput == "BarackObama":
    print("44th president of the United States")
    good = True
if textInput == "SandroPertini":
    print("Former President of the Italian Republic")
    good = True
if textInput == "NelsonMandela":
    print("Former President of South Africa")
    good = True
if textInput == "MahatmaGandhi":
    print("Bapu")
    good = True
if textInput == "DonaldKnuth":
    print("Creator of LaTeX")
    good = True
if textInput == "DennisRitchie":
    print("Creator of C")
    good = True

if good == False:
    print("Invalid input! Please enter a good name!")