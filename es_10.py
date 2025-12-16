#scrivere un programma che generi una lista di numeri
#casuali compresi tra 1,100 che rappresentano misurazioni di intensità
#di un segnale. Il programma dopo aver generato la lista deve essere in
#grado di modificarla in questa maniera: gli elemnti di indice pari
#devono essere azzerati. Inoltre, dopo la modifica, si vuole contare il numero
#di elementisopra una soglia numerica.

#sottoproblemi:
#1) generare una lista di numeri compresi tra 1 e 100.
#2) modificare la lista con laregola sopra
#3) contare il numero di elementi sopra soglia

import random

def generaLista(n):
    mylist=[]
    for i in range(0,n):
       elemento=random.randint(0,100)
       mylist.append(elemento)
    return mylist

def proceduraGeneraLista(n,lista):
    for i in range(0,n):
       elemento=random.randint(0,100)
       lista.append(elemento) 

def modificaLista(lista):
    n=len(lista)
    for i in range(0,n):
        if i % 2 == 0:
            lista[i]=0
      
def soglia(n,lista,nsoglia):
    contatore = 0
    for elemento in range(0,n):
        if lista[i] > nsoglia:
            contatore = contatore + 1
    return contatore

def sogliaIteratore(lista,nsoglia):
    contatore = 0
    for element in lista:
        if elemnt > nsoglia:
            contatore = contatore + 1
    return contatore

listax=generaLista(6)
listap=[]
proceduraGeneraLista(6,listap)
proceduraGeneraLista(lista=listap,n=6)
modificaLista(6,listax)
nsoglia=soglia(6,listax,50) 