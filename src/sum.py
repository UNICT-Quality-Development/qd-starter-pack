def sum_int(a: int, b: int) -> int:
    return a + b

def controllo(mess: list)->int:
    n=""
    while(n.isdecimal()==False): n=input(mess)
    return int(n)
n1=controllo("Inserire il primo numero: ")
n2=controllo("Inserire il secondo numero: ")
print("La somma tra "+str(n1)+"+"+str(n2)+"="+str(sum_int(n1,n2)))

