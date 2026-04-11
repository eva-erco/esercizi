#Analisi delle temperature (°C) settimaneli
#Una stazione meteo ha registrato le temperature di ogni ora per 7 giorni.
#Devi calcolare statistiche giornaliere e trovare la giornata più calda e più
#fredda della settimana struttura dati: lista di liste(7 giorni x 24 ore) 
import random

def riempiTemperature (lista):
    for i in range (0,24):
        lista.append(random.randint(-3,30))
        
def calcola_media(lista):
    somma = 0 
    for i in lista:
        somma = somma + i
    media = somma /len(lista)
    return (media) 


def calcola_varianza(media,lista):
    calcolo = 0
    varianza = 0
    for i in range(0, len(lista)):
        calcolo = (lista[i] - media)**2
        varianza = calcolo + varianza
    varianza = varianza / len(lista) 
    return (varianza)

def deviazione_standard(varianza):
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


if __name__=="__main__":
    lunedi = []
    martedi = []
    mercoledi = []
    giovedi = []
    venerdi = []
    sabato = []
    domenica = []
    riempiTemperature(lunedi)
    riempiTemperature(martedi)
    riempiTemperature(mercoledi)
    riempiTemperature(giovedi)
    riempiTemperature(venerdi)
    riempiTemperature(sabato)
    riempiTemperature(domenica)
    media_lunedi=calcola_media(lunedi)
    media_martedi=calcola_media(martedi)
    media_mercoledi=calcola_media(mercoledi)
    media_giovedi=calcola_media(giovedi)
    media_venerdi=calcola_media(venerdi)
    media_sabato=calcola_media(sabato)
    media_domenica=calcola_media(domenica)
    varianza_lunedi=calcola_varianza(media_lunedi,lunedi)
    varianza_martedi=calcola_varianza(media_martedi,martedi)
    varianza_mercoledi=calcola_varianza(media_mercoledi,mercoledi)
    varianza_giovedi=calcola_varianza(media_giovedi,giovedi)
    varianza_venerdi=calcola_varianza(media_venerdi,venerdi)
    varianza_sabato=calcola_varianza(media_sabato,sabato)
    varianza_domenica=calcola_varianza(media_domenica,domenica)

    print(varianza_lunedi)
    print(varianza_martedi)
    print(varianza_mercoledi)
    print(varianza_giovedi)
    print(varianza_venerdi)
    print(varianza_sabato)
    print(varianza_domenica)

    print(deviazione_standard(varianza_lunedi))
    print(deviazione_standard(varianza_martedi))
    print(deviazione_standard(varianza_mercoledi))
    print(deviazione_standard(varianza_giovedi))
    print(deviazione_standard(varianza_venerdi))
    print(deviazione_standard(varianza_sabato))
    print(deviazione_standard(varianza_domenica))

    print(calcola_moda(lunedi))
    print(calcola_moda(martedi))
    print(calcola_moda(mercoledi))
    print(calcola_moda(giovedi))
    print(calcola_moda(venerdi))
    print(calcola_moda(sabato))
    print(calcola_moda(domenica))

    print(errore_standard(deviazione_standard(varianza_lunedi), lunedi))
    print(errore_standard(deviazione_standard(varianza_martedi), martedi))
    print(errore_standard(deviazione_standard(varianza_mercoledi), mercoledi))
    print(errore_standard(deviazione_standard(varianza_giovedi), giovedi))
    print(errore_standard(deviazione_standard(varianza_venerdi), venerdi))
    print(errore_standard(deviazione_standard(varianza_sabato), sabato))
    print(errore_standard(deviazione_standard(varianza_domenica), domenica))
    
    giorni = [lunedi, martedi, mercoledi, giovedi, venerdi, sabato, domenica]
    medie_sett = media_settimanale(giorni)