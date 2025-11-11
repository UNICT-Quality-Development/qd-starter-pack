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

days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("Inserisci un numero della settimana (1-7)")
week=int(input())

if 1 <= week <= 7:
    indice = week - 1
    day_name= days[indice]
    print(day_name)

else:
    print("Invalid input! Please enter week number between 1-7.")
