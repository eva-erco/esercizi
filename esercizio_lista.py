#data una serie di 10 misurazioni randomiche intere, comprese tra
#2 intervalli forniti da tastiera produrrein output un file di testo che
#abbia i valori, la media dei valori, il numero di valori sopra una certa soglia
#fissata a massimo delle misurazioni meno 10

#1) Creare una lista di 10 misurazioni random (PROCEDURA)
#2) Media dei valori di una lista (FUNZIONE)
#3) Calcolare la soglia [massimo della lista - 10] (FUNZIONE)
#4) Contare il numero di valori sopra la soglia (PROCEDURA)
import random

def creaLista(lista):
    n1=input("Inserire il primo estremo ")
    n1=int(n1)
    n2=input("Inserire il secondo estremo ")
    n2=int(n2)
    
    for i in range(0,10):
        if n1<n2:
            valore=random.randint(n1,n2)
        else:
            valore=random.randint(n2,n1)
        lista.append(valore)

def calcoloMedia(lista):
    somma=0
    for i in range(0,len(lista)):
        somma=somma+lista[i]
    media=somma/len(lista)
    return(media)

def calcoloSoglia(lista):
    massimo=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>massimo:
            massimo=lista[i]
    soglia=massimo-10
    return(soglia)

def contaSopraSoglia(lista,soglia):
    contatore=0
    for i in range(0,len(lista)):
        if lista[i]>soglia:
            contatore=contatore+1
    return(contatore)

if __name__=="__main__":
    listaM=[]
    creaLista(listaM)
    mediaValori=calcoloMedia(listaM)
    soglia=calcoloSoglia(listaM)
    numeroSopra=contaSopraSoglia(listaM,soglia)
    print(mediaValori)
    print(numeroSopra)
