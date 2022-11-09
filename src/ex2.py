#  Improve this program replacing if/else if with an array.
#  Hint:  arr[3] = "Thursday";

if __name__ == '__main__':
  day = input ( "Enter week number(1-7): " )
  week = {0:"Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
  
  if ( int(day) < 7):
    print(week[ int(day) - 1])
  else:
    print("Invalid input! Please enter week number between 1-7.")