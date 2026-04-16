import random
import math
import matplotlib.pyplot as plt  

def riempiTemperature (lista):
    for i in range (0,24):
        lista.append(random.randint(-3,30))

def calcola_media(lista):
    """
    questa funzione calcola la media di un distribuzione numerica
    
    :pares liste: liste unaper giorno contenenti le misurazioni 
    
    """
    somma = 0 
    for i in lista:
        somma = somma + i
    media = somma /len(lista)
    return (media) 


def calcola_varianza(media,lista):
    """
    questa funzione calcola la varianza di un distribuzione numerica
    
    :pares liste: liste una per giorno contenenti le misurazioni
    
    """
    calcolo = 0
    varianza = 0
    for i in range(0, len(lista)):
        calcolo = (lista[i] - media)**2
        varianza = calcolo + varianza
    varianza = varianza / len(lista) 
    return (varianza)


def deviazione_standard(varianza):
    """
    questa funzione calcola la deviazione standard  di un distribuzione numerica
    
    :pares liste: liste unaper giorno contenenti le misurazioni  
    
    """
    devStandard = varianza ** 0.5
    return (devStandard)

def calcola_moda(lista):
    frequenze = {}
    for i in lista:
        if i in frequenze:
            frequenze[i] = frequenze[i] + 1
        else:
            frequenze[i] = 1
        moda = lista[0]
        max_freq = 0
    for i in frequenze:
        if frequenze[i] > max_freq:
            max_freq = frequenze[i]
            moda = i
    return moda


def errore_standard(dev_standard, lista):
    return dev_standard / (len(lista) ** 0.5)


def media_settimanale(liste_giorni):
    medie = []
    for giorno in liste_giorni:
        medie.append(calcola_media(giorno))
    return medie


def giorno_piu_caldo(medie):
    max_temp = medie[0]
    indice = 0
    for i in range(len(medie)):
        if medie[i] > max_temp:
            max_temp = medie[i]
            indice = i
    return indice


def giorno_piu_freddo(medie):
    min_temp = medie[0]
    indice = 0
    for i in range(len(medie)):
        if medie[i] < min_temp:
            min_temp = medie[i]
            indice = i
    return indice

def crea_istogramma(dati, num_bins=10, titolo="Istogramma", colore="skyblue"):
    """
    Crea e visualizza un istogramma a partire da una lista o array di numeri.
 
    :param dati: Lista o array di valori numerici
    :param num_bins: Numero di intervalli (bins) dell'istogramma
    :param titolo: Titolo del grafico
    :param colore: Colore delle barre
    """
    plt.figure(figsize=(8, 5))
    plt.hist(dati, bins=num_bins, color=colore, edgecolor="black", alpha=0.7)
    plt.title(titolo)
    plt.xlabel("Valori")
    plt.ylabel("Frequenza")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()