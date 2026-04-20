#
#  Implement the following code in Python replacing if/else if with an array.
#
#  Hint:  arr[3] = "Thursday";
#

# #include <iostream>
# using namespace std;
#
# int main()
# {
#   int week;
#
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

giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]

try:
    settimana = int(input("Inserisci il numero del giorno della settimana (1-7): "))
    if 1 <= settimana <= 7:
        print(giorni[settimana - 1])
    else:
        print("Input non valido! Inserisci un numero tra 1 e 7.")
except ValueError:
    print("Input non valido! Inserisci un numero intero valido.")
    
