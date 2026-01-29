#scrivere un programma per il calcolo delle radici di un equazione
#di secondo grado
import math

def calcoloDelta(a,b,c):
    delta=(b*b)-(4*a*c)
    return (delta)

def controllaDelta(a,b,delta):
    if delta<0:
        print("impossibile")
    elif delta==0:
        calcoloUnaRadice(a,b)
    else:
        calcoloDueRadici(a,b,delta)

def calcoloUnaRadice(a,b):
    soluzioneUno= -b/2*a
    print (soluzioneUno)
    
def calcoloDueRadici(a,b,delta):
    soluzioneUno= (-b+math.sqrt(delta))/2*a
    print (soluzioneUno)
    soluzioneDue= (-b-math.sqrt(delta))/2*a
    print (soluzioneDue)
    
if __name__ =="__main__":
    
    a=input("Inserisci il coefficente a ")
    a=float(a)
    b=input("Inserisci il coefficente b ")
    b=float(b)
    c=input("Inserisci il coefficente c ")
    c=float(c)
    delta=calcoloDelta(a,b,c)
    print(delta)
    
    controllaDelta(a,b,delta)
    