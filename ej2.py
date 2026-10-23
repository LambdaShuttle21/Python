# EJ 2: Crea 4 hijos sin que los hijos creen mas hijos e 
# imprime su PID

import os

for i in range(4):

    pid = os.fork()

    if pid == 0:
        print(f"Soy el hijo {i + 1} - PID: {os.getpid()}")

        os._exit(0)

for i in range(4):#el padre termina de crear a los 4 hijos en
    #el primer for y ahora hace el .wait aunque ya obviamente todos
    #habran terminado
    os.wait()

print("Todos los hijos han finalizado")
