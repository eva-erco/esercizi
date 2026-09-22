class Atomo:
    def __init__(self,simbolo,numero_atomico,massa):
        #simbolo, numero atomico e massa sono attributi pubblici 
        self.simbolo = simbolo
        if numero_atomico < 0:
            raise ValueError("Il numero atomico deve essere positivo")
        else:
            self.numero_atomico = numero_atomico
        self.massa = massa
        #orbitale è un attributo privato
        self.__orbitale = "2p"
        
    def new_massa(self):
        massa = input("inserisci la nuova massa: ")
        self.massa = float(massa)
    
    def new_orbitale(self):
         orbitale = input("inserisci il nuovo orbitale: ")
         self.orbitale = orbitale  
    
    
    
    def is_stabile(self):
        neutroni = round(self.massa) - self.numero_atomico
        rapporto = neutroni / self.numero_atomico 
        if rapporto >= 0.9 and rapporto <= 1.6:
            return False 
        else:
            return True  

    def printOrbitale(self):
        print(self.__orbitale)
        
    
    def isNobile(self):
        nobili = [2,10,18,36,54,86,118]
        for numero in nubili :
            if numero == self.numero_atomico:
                return True
        #if self.numero_atomico == 2 or srlf.numero :
        #   return True
    def isNobile(self):
        nobili = [2,10,18,36,54,86,118]
        if self.numero_atomico in nobili:
            return True 
    

idrogeno = Atomo("H",1,1.008)
idrogeno.is_stabile()
#per accedere all'esterno ad un attributo pubblico basta usare la sintassi della riga successiva 
print(idrogeno.simbolo)
#per accedere dall'esterno ad un attributo privato devo necesssariamente implementare un metodo 
print(idrogeno.printOrbitale())
idrogeno.new_massa()
idrogeno.new_orbitale()
print(idrogeno.massa)
print(idrogeno.orbitale) 
print(idrogeno.isNobile())



try:
    ferro = Atomo("Fe",-26,55.845)
except ValueError:
    print("Il numero atomico deve essere positivo")