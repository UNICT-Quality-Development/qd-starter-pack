week = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]

n = int(input("choose a number 1-7: "))

if 1<= n <= 7:

    print("Day:", week[n-1])
else:
    print("invalid number!!")