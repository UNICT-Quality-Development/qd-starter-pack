N = [1,2,3,4,5,6,7,8,9]

def f(A:list,k:int)->bool:
    return k in A


def insert_number()->int:
           print("insert a number")
           k = int(input())
           return k


if __name__ == "__main__":
           k = insert_number()
           if((f(N,k) is True)):
               print("number is in the list")
           else:
               print("number is not in the list")

