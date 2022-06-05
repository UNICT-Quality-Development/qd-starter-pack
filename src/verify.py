from typing import List
def isThere(arr:list,val:int,N:int) -> bool:
    for i in range(N):
        if arr[i] == val:
            return True
        
    return False

if __name__ == "__main__":
    arr = [3,4,5,1,2,3,4,9,13,0]
    num = int(input("Insert a number: "))
    print("The number",num, "is" if isThere(arr,num,len(arr)) is True else "is not","present in the array!")