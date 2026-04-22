from jarvis import*

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
    
    crea_istogramma(lunedi)
    crea_istogramma(martedi)
    crea_istogramma(mercoledi)
    crea_istogramma(giovedi)
    crea_istogramma(venerdi)
    crea_istogramma(sabato)
    crea_istogramma(domenica)
    
    covLunMar=covarianza(lunedi,martedi) 
    covLunMer=covarianza(lunedi,mercoledi)
    covLunGio=covarianza(lunedi,giovedi)
    covLunVen=covarianza(lunedi,venerdi)
    covLunSab=covarianza(lunedi,sabato)
    covLunDom=covarianza(lunedi,domenica)

    covMarMer=covarianza(martedi,mercoledi)
    covMarGio=covarianza(martedi,giovedi)
    covMarVen=covarianza(martedi,venerdi)
    covMarSab=covarianza(martedi,sabato)
    covMarDom=covarianza(martedi,domenica)

    covMerGio=covarianza(mercoledi,giovedi)
    covMerVen=covarianza(mercoledi,venerdi)
    covMerSab=covarianza(mercoledi,sabato)
    covMerDom=covarianza(mercoledi,domenica)

    covGioVen=covarianza(giovedi,venerdi)
    covGioSab=covarianza(giovedi,sabato)
    covGioDom=covarianza(giovedi,domenica)

    covVenSab=covarianza(venerdi,sabato)
    covVenDom=covarianza(venerdi,domenica)

    covSabDom=covarianza(sabato,domenica)


    print(covLunMar)
    print(covLunMer)
    print(covLunGio)
    print(covLunVen)
    print(covLunSab)
    print(covLunDom)

    print(covMarMer)
    print(covMarGio)
    print(covMarVen)
    print(covMarSab)
    print(covMarDom)

    print(covMerGio)
    print(covMerVen)
    print(covMerSab)
    print(covMerDom)

    print(covGioVen)
    print(covGioSab)
    print(covGioDom)

    print(covVenSab)
    print(covVenDom)

    print(covSabDom)

    print(correlazione(lunedi,martedi))
    print(correlazione(martedi,mercoledi))
    print(correlazione(mercoledi,giovedi))
    print(correlazione(giovedi,venerdi))
    print(correlazione(venerdi,sabato))
    print(correlazione(sabato,domenica))
    
    