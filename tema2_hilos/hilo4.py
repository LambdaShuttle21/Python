import threading
import time

# Ejercicio: Crea un hilo que le pasemos dos números enteros n1 y n2 y 
# escriba la secuencia comprendida entre ambos números, si n1 < n2.


class hilo(threading.Thread):
    def __init__(self, num1, num2):
        super().__init__()
        self.numero1 = num1
        self.numero2 = num2
    def run(self):
        i = self.numero1
        if self.numero1 < self.numero2:
            print(f"Inicio: {self.numero1} Final {self.numero2}")
            for i in range(self.numero1, self.numero2):
                i = i + 1
                print(i)

print("Inicio")
n1 = int(input("Introduzca n1: "))
n2 = int(input("Introduzca n2: "))
t = hilo(n1, n2)
t.start()
t.join()#espera a que el hilo hijo termine
time.sleep(10)
print("El hilo hijo ha terminado")


