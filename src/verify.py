#
#Write a software that verifies if a number is present in a pre-defined array.
#Output example:
#Insert number 3
#The number 3 is [not] present in the array.


def main():
  N = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
  print("insert number")
  v = input()

  if(int(v) in N): 
    print(f"The number {v} is  present in the array.")
  else:
    print(f"The number {v} is not present in the array.")

if __name__ == "__main__":
    main()


