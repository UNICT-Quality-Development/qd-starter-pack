from random import random
#giocatore 1 lancia 3 dadi 
k = int(random()*10)
z = int(random()*10)
y = int(random()*10)

giocatore1 = [k,z,y]

a = int(random()*10)
b = int(random()*10)
d = int(random()*10)

giocatore2 = [a,b,d]

counterGiocatore1 = 0
counterGiocatore2 = 0

print("Blue dices:")
print(k)
print(z)
print(y)

print("Red dices:")
print(a)
print(b)
print(d)

if giocatore1[0]>giocatore2[0]:
    counterGiocatore1+=1
else:
    counterGiocatore2+=1

if giocatore1[1]>giocatore2[1]:
    counterGiocatore1+=1
else:
    counterGiocatore2+=1

if giocatore1[2]>giocatore2[2]:
    counterGiocatore1+=1
else:
    counterGiocatore2+=1

if counterGiocatore1>=counterGiocatore2:
   print("Giocatore1 ha vinto")
else:
   print("Giocatore2 ha vinto")

