#Programm that prints the Day of the week equal to its number
weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
week = int(input("Enter week number (1-7): "))-1
print("Input not within specified rage") if ((week<0) or (week>6)) else print(weekdays[week])