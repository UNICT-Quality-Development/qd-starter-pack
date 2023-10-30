'''
/* convert in python this code */

#include <iostream>
using namespace std;

int main()
{
  int week;

  /* Input week number from user */
  cout << "Enter week number(1-7): " << endl;
  cin >> week;

  if (week == 1)
  {
    cout << "Monday" << endl;
  }
  else if (week == 2)
  {
    cout << "Tuesday" << endl;
  }
  else if (week == 3)
  {
    cout << "Wednesday" << endl;
  }
  else if (week == 4)
  {
    cout << "Thursday" << endl;
  }
  else if (week == 5)
  {
    cout << "Friday" << endl;
  }
  else if (week == 6)
  {
    cout << "Saturday" << endl;
  }
  else if (week == 7)
  {
    cout << "Sunday" << endl;
  }
  else
  {
    cout << "Invalid input! Please enter week number between 1-7." << endl;
  }

  return 0;
}
'''

x=input('Enter day of the week number(1-7): ')
day_of_week= int(x)

print('\n')

match day_of_week:
    case 1:
      print('its MONDAY\n')
    case 2:
      print('its TUESDAY')
    case 3:
      print('its WEDNESDAY')
    case 4:
      print('its THURSDAY')
    case 5:
      print('its FRIDAY')
    case 6:
      print('its SATURDAY')
    case 7:
      print('its SUNDAY')
    case _:
        print("Invalid input! Please enter week number between 1-7.\n")