import threading
import time


buffer = []# Lista compartida
lock = threading.Lock()

def productor():
    for i in range(5):
        time.sleep(1)  # simula tiempo de producir
        with lock:
            buffer.append(i)
            print(f"Produje {i}")

def consumidor():
    while True:
        with lock:
            if buffer:  # si hay algo en la lista
                item = buffer.pop(0)#si guarde un 1, item = 1 y se elimina de buffer[]
                print(f"Consumí {item}")
                if item == 4:  # última señal para terminar
                    break
        time.sleep(2)  # simula tiempo de consumir

# Crear hilos
h1 = threading.Thread(target=productor)
h2 = threading.Thread(target=consumidor)

h1.start()
h2.start()

h1.join()
h2.join()

print("Fin del programa")
