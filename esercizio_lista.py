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
    n2=input("Iserire il secondo estremo ")
    n2=int(n2)
    for i in range (0,10):
        if n1>n2:
            valori=random.randint(n1,n2)
        else:
            valori=random.randint(n2,n1)
        lista.append(valori)
        
def calcoloMedia(lista):
    somma=0
    for i in range(0,len(lista)):
        somma=somma+lista[i]
    media=somma/len(lista)
    return(media)
        
def calcoloSoglia(lista):
    max=
    
    
if __name__=="__main__":
    listaM=[]
    creaLista(listaM)
    mediValori=calcolo_media(listaM) 
    
    