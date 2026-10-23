import threading
import time
import random

#método al que se va a asociar el hilo
class hilo(threading.Thread):
    def run(self):
        time.sleep(random.random())
        print("Hola en el hijo")

t = hilo()
t.start()
t.join()
time.sleep(random.random())
print ("Hola en el padre") #impresión en el hilo principal

