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

def get_weekday(week: int) -> str:
    """Return the weekday corresponding to a number from 1 to 7."""
    match week:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid input! Please enter a number between 1 and 7."


def main() -> None:
    """Read a week number and print the corresponding weekday."""
    try:
        week = int(input("Enter week number (1-7): "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    print(get_weekday(week))


if __name__ == "__main__":
    main()
