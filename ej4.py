numeros = [8, 3, 12, 5, 20, 7, 14, 9]
mitad = len(numeros)/2

primera_mitad = numeros[:mitad]
segunda_mitad = numeros[mitad:]

import os

pares_primera_mitad = []
impares_segunda_mitad = []

pid1 = os.fork()#bifurcacion, se crea al hijo1 y el 
#se encarga de meter los pares sin crear mas hijos

if pid1 == 0:#en la bifurcacion pid1 = 0 es el proceso hijo
    for numero in primera_mitad:
        if numero % 2 == 0:
            pares_primera_mitad.append(numero)#agrego
    print(f"Pares del hijo 1 PID {os.getpid()}: \n")
    print(pares_primera_mitad)
    os._exit(0)#sale del proceso hijo

else:#mientras hijo1 labura, padre se mete en else y crea hijo2
    #o pid2
    pid2 = os.fork()
    if pid2 == 0:
        for numero in segunda_mitad:
            if numero % 2 != 0:
                    impares_segunda_mitad.append(numero)
        print(f"Impares del hijo 2 PID {os.getpid()}: \n")
        print(impares_segunda_mitad)
        os._exit(0)#sale del proceso hijo

