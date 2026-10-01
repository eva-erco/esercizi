class CampioneDNA:
    def __init__(self,codice_campione,sequenza,laboratorio,geni_mappati=[],mutazioni_rilevate={}):
        self.__codice_campione = codice_campione
        self.__sequenza = sequenza
        self.__geni_mappati = geni_mappati
        self.__mutazioni_rilevate = mutazioni_rilevate
        self.laboratorio = laboratorio

    def aggiungi_gene(self,gene):
        if gene not in self.__geni_mappati:
            self.__geni_mappati.append(gene)

    def registra_mutazione(self,posizione,tipo):
        self.__mutazioni_rilevate[posizione] = tipo

    def calcola_percentuale_gc(self):
        gc = 0
        for base in self.__sequenza:
            if base == "G" or base == "C":
                gc = gc + 1
        percentuale = gc / len(self.__sequenza) * 100
        return percentuale

    def stampa_report(self):
        print(self.__codice_campione)
        print(self.laboratorio)
        print(self.__sequenza)
        print(self.__geni_mappati)
        print(self.__mutazioni_rilevate)
        print(self.calcola_percentuale_gc())

campione = CampioneDNA("DNA-4029","ATCGGCTAGCTAGCGGATCG","LabGen-BioApp")

campione.aggiungi_gene("geneA")
campione.aggiungi_gene("ampR")
campione.aggiungi_gene("lacZ")

campione.registra_mutazione(45,"sostituzione")
campione.registra_mutazione(120,"delezione")

campione.stampa_report()
