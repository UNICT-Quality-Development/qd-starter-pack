#Generatore Numero Casuale (Esempio - Lancio di dadi)
import random
x = int(input("Quanti lanci vuoi fare? "))
results = random.choices(range(1, 7), k=x)
for i in range(len(results)):
    print("Lancio",i+1,": ",results[i],"\n")