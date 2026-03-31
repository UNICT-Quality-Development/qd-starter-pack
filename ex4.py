#Program that associates a Month number to its name and amount of days in it
months = {
    1:"January, 31 days",
    2:"February, 28/29 days",
    3:"March, 31 days",
    4:"April, 30 days",
    5:"May, 31 days",
    6:"June, 30 days",
    7:"July, 31 days",
    8:"August, 31 days",
    9:"September, 30 days",
    10:"October, 31 days",
    11:"November, 30 days",
    12:"December, 31 days"
}

print(months.get(int(input("Input month number (1-12): ")), "Incorrect Input!"))