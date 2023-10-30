week = int(input('Enter week number (1-7): '))

week_days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6:'Saturday', 7: 'Sunday'}

if week in week_days:
    print(week_days[week])
else:
    print('Invalid week number')
