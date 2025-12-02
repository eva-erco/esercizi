#scrivere una funzione che dati due numeri interi restituisca il maggiore

def nMaggiore (numero1,numero2):
    if numero1>numero2:
        return numero1
    else:
        return numero2
#scrivere una procedura che dato un numero stampi a video
#se è pari o dispari
    
def nPariDispari (numero1):
    if numero1%2==0:
        print("Il numero è pari")
    else:
        print("Il numero è dispari")

uno=input("inserire il primo numero ")
uno=int(uno)
due=input("inserire il secondo numero ")
due=int(due)

risultato=nMaggiore(uno,due)
print(risultato)
nPariDispari(risultato)

#con questo esercizio ho creato un programma che dati due interi stampi a video
#se il maggiore è pari o dispari


