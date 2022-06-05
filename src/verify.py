from typing import List
def is_there(arr:list[int],val:int,N:int) -> bool:
    for i in range(N):
        if arr[i] == val:
            return True
        
    return False

def main(): # pragma: no cover
    arr = [3,4,5,1,2,3,4,9,13,0]
    num = int(input("Insert a number: "))
    print("The number",num, "is" if is_there(arr,num,len(arr)) else "is not","present in the array!")    

if __name__ == "__main__": # pragma: no cover
    main()    