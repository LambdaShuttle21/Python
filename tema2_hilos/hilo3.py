import threading
import random
import time

class corredor(threading.Thread):
    def __init__(self, dorsal, nombre):
        super().__init__() #siempre se debe poner, invoca a la función init de la clase padre, la de Thread
        self. dorsal = dorsal
        self.nombre = nombre
    def run(self):
       time.sleep(random.uniform(0.5, 3))
       print(f" Dorsal {self.dorsal}: {self.nombre} cruza la meta")

nombres = ["Rayo", "Tortuga", "Cohete", "Caracol"]

hilos = []
for i, nombre in enumerate(nombres, start=1):
    t = corredor(i, nombre)
    t.start()
    hilos.append(t)

for t in hilos:
    t.join()

print("Carrera terminada")
