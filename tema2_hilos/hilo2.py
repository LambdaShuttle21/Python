# ‘’’
# En este código se aprende cómo almacenar hilos en listas (arrays). Nos será útil.
# Escribir y probar.
# ‘’’

import threading

class hilo(threading.Thread):
    def __init__(self, numHilo):
        super().__init__()
        self.numero = numHilo
    def run(self):
        print (f"Escribo desde el hilo {self.numero}")

print ("INICIO")
hilos = list() #En java sería ‘ArrayList<¿tipo?> lista = new ArrayList<>()

for i in range(50):
    t = hilo(i)
    hilos.append(t) #En java sería hilos.add(t)
    t.start()

print ("ESCRIBO EN PRINCIPAL")
