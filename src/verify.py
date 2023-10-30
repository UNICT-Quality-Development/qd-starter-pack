N = [1,2,3,4,5,6,7,8,9]

def f(A:list)->bool:
    print("insert a number")
    k = int(input())
    if (k in A):
        print("number is in the list") 
    else:
         print("number is not in the list")

f(N)
