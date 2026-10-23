'''
Crea un programa en Python que:

- Pida al usuario un número N (cantidad de procesos hijos a crear).

- Use os.fork() para crear N procesos hijos.

 -Cada hijo debe imprimir:

    Su número de proceso (PID).

    El número de orden en el que se cre (1<=numero<=N).

    Una pausa aleatoria entre impresiones (para simular trabajo), entre 1 y 2 minutos.
'''

import os
import random
import time


cantidadHijos = int(input("Cantidad de hijos a crear: "))

for i in range(0, cantidadHijos):
    pid = os.fork()#bifurcacion de procesos, padre e hijo 
    #hijo es 0 y padre tiene el pid del hijo xxxx

    if pid == 0:
        #imprimo
        print(f"Hijo {i+1} con PID: {os.getpid()}")
        #hijo duerme entre 1 y 2 min 
        time.sleep(random.randint(60, 120))
        #hijo sale para que no cree mas procesos en el for
        os._exit(0)

for i in range(cantidadHijos):#espera al hijo1, hijo2, hijo3, etc...
    #los espera de forma individual a que terminen
    os.wait()
