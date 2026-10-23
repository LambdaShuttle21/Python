import os

numeros = [4, 7, 2, 9, 5]

for numero in numeros:
    pid = os.fork()
    cuadrado = 0

    if pid == 0:
        cuadrado = numero ** 2
        print(f"Hijo PID {os.getpid()} -> {numero}² = {cuadrado}")
        os._exit(0)

for _ in numeros:
    os.wait()

print("Todos los hijos finalizados")