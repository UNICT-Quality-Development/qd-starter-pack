from random import randint

def sum(a: float, b: float)-> float:
    return a + b

def difference(a: float, b: float)-> float:
    return a - b

def multiplication(a: float, b: float)-> float:
    return a * b

def division(a: float, b: float)-> float:
    return a / b    

def first_number()-> float:
    print("Insert first number:")
    first_number = float ( input() )

    return first_number

def second_number()-> float:
    print("Insert second number:")
    second_number = float ( input() )   

    return second_number
     
def calculate()-> float:  
    first_num = first_number()
    second_num = second_number()  
    random_num = randint(0, 3)

    match random_num:  
        case 0: 
            return sum(first_num, second_num)
        case 1: 
            return difference(first_num, second_num)
        case 2: 
            return multiplication(first_num, second_num) 
        case 3:  
            return division(first_num, second_num)   
