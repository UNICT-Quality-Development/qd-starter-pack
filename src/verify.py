N = [1,2,3,4,5,6,7,8,9]

def f(A:list,k:int)->bool:
    if (k in A):
        return True
    else:
        return False


print("insert a number")
k = int(input())

if((f(N,k))==True):
    print("number is in the list")
else:
    print("number is not in the list")

