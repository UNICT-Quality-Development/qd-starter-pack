def calculate(x:float,y:float,op:str) -> float:
    match op:  
        case "S": 
            return x+y
        case "D": 
            return x-y
        case "M": 
            return x*y
        case "d": 
            if y == 0:
              print("ERROR, IMPOSSIBLE TO DIVIDE BY ZERO!","\n","\n") 
              return 0
            else:
              return x/y    

if __name__ == "__main__":
    x = float(input("Inserisci un numero:"))
    y = float(input("Inserisci un numero:"))

    print()
    print("Sum: ", calculate(x,y,"S"))
    print("Difference: ", calculate(x,y,"D"))
    print("Multiplication: ", calculate(x,y,"M"))
    print("Division: ", calculate(x,y,"d"))
