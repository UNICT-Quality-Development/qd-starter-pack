# Programma per generare numeri randomici...
# Utilizzando il potere DEL TEMPO:

import time


def gen_number() -> int:
    return int(str(time.time())[-2])


# prendiamo la parte che rappresenta i millisecondi
# siccome cambiano estremamente velocemente, appariranno randomici

# visualizziamo 10 risultati
RESULTS_TO_DISPLAY = 10
results = [0 for i in range(RESULTS_TO_DISPLAY)]

for _ in range(10**5):
    results[gen_number()] += 1

print(results)
