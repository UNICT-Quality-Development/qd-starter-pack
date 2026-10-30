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


def get_day_of_week(week: int) -> str:
    if week == 1:
        day = "Monday"
    elif week == 2:
        day = "Tuesday"
    elif week == 3:
        day = "Wednesday"
    elif week == 4:
        day = "Thursday"
    elif week == 5:
        day = "Friday"
    elif week == 6:
        day = "Saturday"
    elif week == 7:
        day = "Sunday"
    else:
        day = "Invalid input! Please enter week number between 1-7."
    return day


print("Enter week number(1-7): ")
try:
    input = int(input())
    print(get_day_of_week(input))
except ValueError:
    print("Invalid input! Please enter week number between 1-7.")
