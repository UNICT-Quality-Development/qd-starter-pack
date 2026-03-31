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


def main():
    week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    day = int(input("Enter week number(1-7): "))

    if 0 < day < 8:
        print(week[day-1])
    else:
        print("Invalid input! Please enter week number between 1-7.")



if __name__ == "__main__":
    main()
