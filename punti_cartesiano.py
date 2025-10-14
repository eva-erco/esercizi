#dato un'insieme di 20 punti su un piano cartesiano,
#random compresi nell'intervallo 0,10. Calcolare il
#punto con ascissa massima e il punto con ordinata minima.

import random

x=[]
y=[]
for i in range(0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))
    
#ascissa massima ?
#scorrere la lista delle x, trovare il massimo e salvare l'indice
#visualizzare poi con un print il numero
massimo=x[0]

for i in range(0,20):
    if x[i]>massimo:
        massimo=x[i]
print(massimo,y[massimo])    

#ordinata minima ?
#scorrere la lista delle y, trovare il minimo e salvare l'indice
#visualizzare poi con un print il numero
minimo=y[0]

for i in range(0,20):
    if y[i]<minimo:
        minimo=y[i]
print(minimo,x[minimo])

punti_cartesiano=[]
for i in range(0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)
    
#come accedere alla x del primo punto
print(punti_cartesiano[0][0])
#come accedere alla y del primo punto
print(punti_cartesiano[0][1])

