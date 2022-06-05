from random import randint

def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b    

def first_number():
    print("Insert first number:")
    first_number = float ( input() )

    return first_number

def second_number():
    print("Insert second number:")
    second_number = float ( input() )   

    return second_number
     
def calculate():  
    first_num = first_number()
    second_num = second_number()  
    random_num = randint(0, 3)

    match random_num:  
        case 0: 
            sum_result = sum(first_num, second_num)
            return sum_result
        case 1: 
            difference_result = difference(first_num, second_num)
            return difference_result
        case 2: 
            multiplication_result = multiplication(first_num, second_num) 
            return multiplication_result
        case 3: 
            division_result = division(first_num, second_num) 
            return division_result  
