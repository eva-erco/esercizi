#scrivere un programma che dati due numeri interi random
#in un intervallo 0,100 ne calcoli lasomma, necalcoli la differenza
#e controlli se la differenza è minore di una certa soglia fissata
#a priori nel main.
#sottoproblemi:
#1) Somma di due numeri (procedura)
#2) Differenza tra due nuemeri (funzione) 
#3) Verificare se un numero è minore di una soglia (procedura)
import random

def calcoloSomma(a, b):
    somma = a + b
    print(somma)

def calcoloDifferenza(a, b):
    differenza = a - b
    return differenza

def calcoloSoglia(numero, soglia):
    if numero < soglia:
        print("La differenza è minore della soglia")
    else:
        print("La differenza è maggiore della soglia")

if __name__ == "__main__":
    soglia = 20
    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)

    print(numero1, numero2)

    calcoloSomma(numero1, numero2)

    differenza = calcoloDifferenza(numero1, numero2)
    print(differenza)

    calcoloSoglia(differenza, soglia)

