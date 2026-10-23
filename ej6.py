#Crear 3 procesos hijos usando un os.fork()

import os

for i in range(3):
    pid = os.fork()
    if pid == 0:
        print(f"Hola, soy el proceso {i+1} con pid {os.getpid()}")
        #sale del hijo para que no vuelva arriba a crear mas hijos, solo el padre
        os._exit(0)

for _ in  range(3):
    os.wait()
print(f"El proceso padre con pid {os.getpid()} ha terminado")