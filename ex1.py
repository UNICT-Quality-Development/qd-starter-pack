"""/* Improve this program using a switch-case. */

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
}"""

Week = input("Inserisci un numero da 1 a 7:")
n = int(Week)

if n < 1 or n > 7:
    print ("Errore, i numeri inseriti non sono corretti.")


match Week:
    case "1":
        print("Lunedì")
    case "2":
        print("Martedì")
    case "3":
        print("Mercoledì")
    case "4":
        print("Giovedì")
    case "5":
        print("Venerdì")
    case "6":
        print("Sabato")
    case "7":
        print("Domenica")