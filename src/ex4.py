
day = input("Enter month number(1-12): ")

nums = ["31 days", "28/29 days", "30 days","Invalid input! Please enter month number between 1-12"]
if int(day) >= 1 and int(day) <= 12:
    if(int(day) == 2):
        print(nums[1])
    elif(int(day) == 11 or int(day) == 9 or int(day) == 6 or int(day) == 4):
         print(nums[0])
    else:
      print(nums[2])
else:
    print(nums[3])
