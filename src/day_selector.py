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
#   return 0;
# 
def week_day():
 week = int(input("Enter week number (1-7):"))
 if week == 1: print("Monday")
 elif week == 2: print("Tuesday")
 elif week == 3: print("Wednesday")
 elif week == 4: print("Thursday")
 elif week == 5: print("Friday")
 elif week == 6: print("Saturday")
 elif week == 7: print("Sunday")
 else: print("Invalid input! Please enter week number between 1-7")
week_day()
