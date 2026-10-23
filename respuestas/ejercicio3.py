'''
Escribe un programa en Python que:

Pida al usuario un número entero positivo N (por ejemplo, N = 100).
Se crean 2 procesos hijo.
El primer hijo buscará y contará los números primos en el rango [2, N//2].
El segundo hijo buscará y contará los números primos en el rango [N//2 + 1, N].
Cada hijo imprimirá cuántos primos encontró en su rango y la lista de los mismos.
'''

import os

def hijo(inicio, final):
    primos = 0
    lista=[]
    for numero in range(inicio, final+1):
        es_primo = True
        divisor = 2
        while es_primo and (divisor < numero):
            es_primo = (numero % divisor != 0)
            divisor+=1
        
        if es_primo:
            primos += 1
            lista.append(numero)
    
    print(f"En el rango desde {inicio} hasta {final} el número de primos es {primos}")
    print(f"Lista {lista}")
    os._exit(0)

rango = int(input("Introduce rango: "))
mitad = rango // 2
pid = os.fork()

if (pid==0):
    hijo(2, mitad)

pid = os.fork()
if (pid == 0):
    hijo(mitad+1, rango)



