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
    match week:
        case 1:
            day = "Monday"
        case 2:
            day = "Tuesday"
        case 3:
            day = "Wednesday"
        case 4:
            day = "Thursday"
        case 5:
            day = "Friday"
        case 6:
            day = "Saturday"
        case 7:
            day = "Sunday"
        case _:
            day = "Invalid input! Please enter week number between 1-7."
    return day


if __name__ == "__main__":
    try:
        settimana = int(input("Enter week number(1-7): "))
        print(get_day_of_week(settimana))
    except ValueError:
        print("Invalid input! Please enter week number between 1-7.")