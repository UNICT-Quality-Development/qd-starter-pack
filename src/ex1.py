# Implement this exercise from C++ to Python
#

# #include <iostream>
# using namespace std;
#
# int main()
# {
#   int week;
#
#   /* Input week number from user */
#   cout << "Enter week number(1-7): " << endl;
#   cin >> week;
#
#   if (week == 1)
#   {
#     cout << "Monday" << endl;
#   }
#   else if (week == 2)
#   {
#     cout << "Tuesday" << endl;
#   }
#   else if (week == 3)
#   {
#     cout << "Wednesday" << endl;
#   }
#   else if (week == 4)
#   {
#     cout << "Thursday" << endl;
#   }
#   else if (week == 5)
#   {
#     cout << "Friday" << endl;
#   }
#   else if (week == 6)
#   {
#     cout << "Saturday" << endl;
#   }
#   else if (week == 7)
#   {
#     cout << "Sunday" << endl;
#   }
#   else
#   {
#     cout << "Invalid input! Please enter week number between 1-7." << endl;
#   }
#
#   return 0;
# }

if __name__ == "__main__":
    week = input("Che giorno è oggi? (1-7)")

    if week == "1":
        print("Lunedi")
    elif week == "2":
        print("Martedi")
    elif week == "3":   
        print("Mercoledi")
    elif week == "4":
        print("Giovedi")
    elif week == "5":
        print("Venerdi")
    elif week == "6":
        print("Sabato")
    elif week == "7":
        print("Domenica")
    else:
        print("Input non valido! Inserisci un numero tra 1 e 7.")
  
