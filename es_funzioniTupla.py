#Dati quattro numeri interi generati random creare una tupla che contenga
#il maggiore dei primi due e il minore dei secondi due.

#sottoproblemi: trovare il maggiore di due numeri
#               trovare il minore di due numeri
import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3 = random.randint(1, 10)
num4 = random.randint(1, 10)

print("numeri generati:", num1,num2,num3,num4)

def nMaggiore (numero1, numero2):
    if numero1>numero2:
        return numero1
    else:
        return numero2

def nMinore (numero1, numero2):
    if numero1<numero2:
        return numero1
    else:
        return numero2

risultato=(nMaggiore(num1,num2),nMinore(num3,num4))
print("Il maggiore dei primi due e il minore degli ultimi due sono:", risultato)