class CampioneDNA:
    """Rappresenta un campione di DNA e le informazioni associate."""

    def __init__(self, codice_campione, sequenza, laboratorio,
                 geni_mappati=[], mutazioni_rilevate={}):
        """Inizializza un nuovo campione di DNA.

        Args:
            codice_campione (str): Codice identificativo del campione.
            sequenza (str): Sequenza di DNA del campione.
            laboratorio (str): Nome del laboratorio che analizza il campione.
            geni_mappati (list, optional): Lista dei geni mappati.
                Il valore predefinito è una lista vuota.
            mutazioni_rilevate (dict, optional): Dizionario contenente
                le mutazioni rilevate, associate alla loro posizione.
                Il valore predefinito è un dizionario vuoto.
        """
        self.__codice_campione = codice_campione
        self.__sequenza = sequenza
        self.__geni_mappati = geni_mappati
        self.__mutazioni_rilevate = mutazioni_rilevate
        self.laboratorio = laboratorio

    def aggiungi_gene(self, gene):
        """Aggiunge un gene alla lista dei geni mappati.

        Il gene viene aggiunto solo se non è già presente nella lista.

        Args:
            gene (str): Nome del gene da aggiungere.
        """
        if gene not in self.__geni_mappati:
            self.__geni_mappati.append(gene)

    def registra_mutazione(self, posizione, tipo):
        """Registra una mutazione rilevata nel campione.

        Args:
            posizione (int): Posizione della mutazione nella sequenza
                di DNA.
            tipo (str): Tipo di mutazione rilevata, ad esempio
                "sostituzione" o "delezione".
        """
        self.__mutazioni_rilevate[posizione] = tipo

    def calcola_percentuale_gc(self):
        """Calcola la percentuale di basi G e C nella sequenza di DNA.

        Returns:
            float: Percentuale di basi G e C presenti nella sequenza.
        """
        gc = 0
        for base in self.__sequenza:
            if base == "G" or base == "C":
                gc = gc + 1

        percentuale = gc / len(self.__sequenza) * 100
        return percentuale

    def stampa_report(self):
        """Stampa a video un report con le informazioni del campione.

        Il report contiene il codice del campione, il laboratorio,
        la sequenza di DNA, i geni mappati, le mutazioni rilevate
        e la percentuale di GC.
        """
        print(self.__codice_campione)
        print(self.laboratorio)
        print(self.__sequenza)
        print(self.__geni_mappati)
        print(self.__mutazioni_rilevate)
        print(self.calcola_percentuale_gc())


campione = CampioneDNA(
    "DNA-4029",
    "ATCGGCTAGCTAGCGGATCG",
    "LabGen-BioApp"
)

campione.aggiungi_gene("geneA")
campione.aggiungi_gene("ampR")
campione.aggiungi_gene("lacZ")

campione.registra_mutazione(45, "sostituzione")
campione.registra_mutazione(120, "delezione")

campione.stampa_report()