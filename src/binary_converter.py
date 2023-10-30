def binary_converter(decimale: int) -> str :
    b = ''
    
    while decimale > 0:
        
        if decimale % 2 == 0:
            b = '0' + b
        else:
            b = '1' + b
            
        decimale = int(decimale / 2)
    
    return b

a = int(input('Inserisci un numero decimale intero: '))
c = binary_converter(a)
print("Rappresentazione binaria. " + c)