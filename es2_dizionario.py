"""
1)Estrarre 3 carte da un mazzo(lista) [1,2,3,4,5,6,7,8,9,10,J,Q,K]
2)Calcolare punteggio usando dizionario che associ ad ogni carta il suo valore

"""

import random

somma=0
mazzo=[1,2,3,4,5,6,7,8,9,10,"J","Q","K"]

carte_estratte=random.sample(mazzo,3)


#indice= random.randint(1,13)
#carta_estratta=mazzo[indice]

#codice A 
mydict={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"J":10,"Q":10,"K":10}

for i in range(0,3):
    indice=random.randint(1,13)
    carte_estratte=mazzo[indice]
    valore=bj[carte_estratte]
    somma=somma+valore
  
  
#codice B
    


  