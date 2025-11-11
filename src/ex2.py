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


arr = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]

week = input("Enter week number(1-7): ")

try:
    week = int(week)-1
except:
    print("The given value is not a number")
    exit(1)

if week < 0 or week > 7:
    print("Invalid input! Please enter week number between 1-7.")
    exit(1)

print(arr[week])
