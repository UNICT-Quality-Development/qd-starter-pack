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

def checkDay(toCheck):
    if toCheck == 1:
        print("Monday")
    elif toCheck == 2:
        print("Tuesday")
    elif toCheck == 3:
        print("Wednesday")
    elif toCheck == 4:
        print("Thursday")
    elif toCheck == 5:
        print("Friday")
    elif toCheck == 6:
        print("Saturday")
    elif toCheck == 7:
        print("Sunday")
    else:
        print("Invalid input! Please enter day number between 1-7.")

day = int(input("Enter day number(1-7): "))
checkDay(day)
