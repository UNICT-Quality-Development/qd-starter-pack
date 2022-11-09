week = ("Monday", "Tuesday", "Thursday", "Friday", "Saturday", "Sunday")


print("Enter week number(1-7): ")
n = int(input())

try:
    print(week[n])
except:
    print("Invalid number")