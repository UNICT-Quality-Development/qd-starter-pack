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

weekday = ["Monday","Tuesday","Wednesday", "Thursday","Friday","Saturday","Sunday"]

day = int(input("Enter week number (1-7): "))

while day not in range(1,len(weekday)+1):
    day = int(input("You didn't enter a valid number!\nValid numbers: 1 to 7\n"))
print(weekday[day - 1])
