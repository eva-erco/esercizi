def sommaLista (lista):
    somma=0
    for element in lista:
        somma=somma+element
    print(somma)
   
def numPari (lista):
    contatore=0
    for element in lista:
        if element % 2 == 0:
            contatore=contatore+1 
    print(contatore)
    
lista = [1,2,3,4]
sommaLista(lista)
numPari(lista)
lista2 = [2,3,4,5]
sommaLista(lista2)
numPari(lista2)