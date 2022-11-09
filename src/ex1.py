weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
value = int(input("Insert a number (from 1 to 7): "))

while value < 1 or value > 7:
    print(f'{value} is not a valid value\n')
    value = int(input("Insert a number (from 1 to 7): "))
else:
    print(f'Day selected: {weeks[value-1]}')