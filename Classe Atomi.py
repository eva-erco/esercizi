class Atomo:
    def __init__(self,massa,simbolo,numero_atomico):
        if numero_atomico < 0:
            raise ValueError("Il numero atomico deve essere positivo")
        self.massa = massa
        self.simbolo = simbolo
        self.numero_atomico = numero_atomico
        
    def stabile(self):
        self.neutroni = round(self.massa) - self.numero_atomico
        if 0.9 <= neutroni/numero_atomico <= 1.6:
            print ("é stabile")
        else:
            print("Non è stabile") 

            




idrogeno = Atomo(1.008,"H",1)
try:
    ferro = Atomo(55.845,"Fe",-26)
except ValueError:
    print("Il numero atomico deve essere positivo")

