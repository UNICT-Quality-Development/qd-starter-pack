
days = ["Invalid input! Please enter week number between 1-7.","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
   


week = input("Enter week number(1-7): ")
week_int = int(week)

if(week_int >= 1 and week_int <= 7):
    print(days[week_int])
else:
    print(days[0])








