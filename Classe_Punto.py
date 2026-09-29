import math

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def is_ascissa(self):
        if self.y == 0:
            return True
        else:
            return False 
    def is_ordinata(self):
        if self.x == 0:
            return True 
        else:
            return False

    def distanza(self,secondoPunto):
        primoTermine = (self.x-secondoPunto.x)**2
        secondoTermine = (self.y-secondoPunto.y)**2
        distanza = math.sqrt(primoTermine+secondoTermine)
        print (distanza)
        

primPunto = Punto(2,3)
secondoPunto = Punto(1,1)
primPunto.distanza(secondoPunto)

if primPunto.is_ascissa() == True:
    print("Il punto appartiene all'asse delle x ")
else:
    print("Il punto non appartiene all'asse delle x ")
    
if primPunto.is_ordinata() == True:
    print("Il punto appartiene all'asse delle y ")
else:
    print("Il punto non appartiene all'asse delle y ")
    
if secondoPunto.is_ascissa() == True:
    print("Il punto appartiene all'asse delle x ")
else:
    print("Il punto non appartiene all'asse delle x ")
    
if secondoPunto.is_ordinata() == True:
    print("Il punto appartiene all'asse delle y ")
else:
    print("Il punto non appartiene all'asse delle y")

 
