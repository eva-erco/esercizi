class Filosofo:
    def __init__(self, nome, anno):
        self.nome = nome
        self.anno = anno

    def caratteristiche(self):
        print("Nome:", self.nome)
        print("Anno:", self.anno)


class ScuolaFilosofica:
    def __init__(self, nome, fondatore, epoca, filosofi=[]):
        self.nome = nome
        self.fondatore = fondatore
        self.epoca = epoca
        self.filosofi = filosofi.copy()

    def descrivi(self):
        print("Nome scuola:", self.nome)
        print("Fondatore scuola:", self.fondatore)
        print("Epoca:", self.epoca)

    def stampa_filosofi(self):
        for filosofo in self.filosofi:
            filosofo.caratteristiche()

    def aggiungi_filosofo(self, filosofo):
        self.filosofi.append(filosofo)


class Stoicismo(ScuolaFilosofica):
    def __init__(self, nome, fondatore, epoca, filosofi, valore_virtu_principale):
        super().__init__(nome, fondatore, epoca, filosofi)
        self.valore_virtu_principale = valore_virtu_principale

    def descrivi(self):
        print("Nome scuola:", self.nome)
        print("Fondatore scuola:", self.fondatore)
        print("Epoca:", self.epoca)
        print("Valore virtù principale:", self.valore_virtu_principale)


class Epicureismo(ScuolaFilosofica):
    def __init__(self, nome, fondatore, epoca, filosofi, piacere_perseguito):
        super().__init__(nome, fondatore, epoca, filosofi)
        self.piacere_perseguito = piacere_perseguito

    def descrivi(self):
        print("Nome scuola:", self.nome)
        print("Fondatore scuola:", self.fondatore)
        print("Epoca:", self.epoca)
        print("Piacere perseguito:", self.piacere_perseguito)


f1 = Filosofo("Zenone di Cizio", 334)
f2 = Filosofo("Seneca", 4)
f3 = Filosofo("Marco Aurelio", 121)
f4 = Filosofo("Epicuro", 341)
f5 = Filosofo("Metrodoro", 331)

stoicismo = Stoicismo("Stoicismo","Zenone di Cizio","Età ellenistica",[f1, f2],"Virtù")

epicureismo = Epicureismo("Epicureismo","Epicuro","Età ellenistica",[f4],"Piacere catastematico")

stoicismo.descrivi()
epicureismo.descrivi()

stoicismo.aggiungi_filosofo(f3)
epicureismo.aggiungi_filosofo(f5)

stoicismo.stampa_filosofi()
epicureismo.stampa_filosofi()
