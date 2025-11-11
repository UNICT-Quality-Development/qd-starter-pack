week = int(input("Enter week number (1-7): "))

print("You entered:", week)

if week == 1:
    print("Monday")
elif week == 2:
    print("Tuesday")
elif week == 3:
    print("Wednesday")
elif week == 4:
    print("Thursday")
elif week == 5:
    print("Friday")
elif week == 6:
    print("Saturday")
elif week == 7:
    print("Sunday")
else:
    print("Invalid input! Please enter number between 1-7.")