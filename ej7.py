#Crear 5 hijos con fork
# cada hijo debe sumar numros del 1 a n, donde n = pid
# del hijo % 100
# imprimir su pid y el resultado de la suma
# terminar correctamente con os._exit(0)


import os

for i in range(5):
    pid = os.fork()
    if pid == 0:
        n = os.getpid() % 100
        suma = 0
        for num in range(1, n+1):
            suma = suma + num
            #sale del hijo para que no vuelva arriba a crear mas hijos, solo el padre
        print(f"Hola, soy el proceso {i+1} con pid {os.getpid()} y la suma es: {suma}")
        os._exit(0)

for _ in  range(5):
    os.wait()
print(f"El proceso padre con pid {os.getpid()} ha terminado")