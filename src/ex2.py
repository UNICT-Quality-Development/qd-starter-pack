week = int(input('Enter week number (1-7): '))

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(week_days[week - 1] if week in range(1, 8) else 'Invalid week number')
