# El padre tiene una lista de 3 "archivos" simulados (cada uno 
# es a su vez una lista de líneas de texto, como si fueran 
# logs de un servidor). Crea 3 hijos, uno por archivo: 
# cada hijo debe recorrer su lista de líneas y contar cuántas 
# contienen la palabra "ERROR", luego imprimir el resultado. 
# El padre crea los 3 sin esperar entre ellos, y al final los
#  espera a todos.
# Pistas

# Recorre la lista archivos para ir sacando cada log de la forma 
# for archivo in archivos:

# Buscar una palabra dentro de una línea se hace con el operador
#  in: if "ERROR" in linea devuelve True o False directamente.

# Como cada hijo sólo necesita imprimir su resultado 
# (no devolver nada al padre), no hace falta código de
#  salida especial: basta con os._exit(0).

# Esquema en la siguiente página:

import os

archivos = [
["INFO login ok", "ERROR timeout", "INFO logout ok"], 
["ERROR db down", "ERROR db down", "INFO retry ok"], 
["INFO ok", "INFO ok", "INFO ok"],
]


for archivo in archivos:
    pid = os.fork()#padre vuelve y crea hijo 1,2 y 3

    if pid == 0:

        contador = 0

        for linea in archivo:
              if "ERROR" in linea:
                contador = contador + 1
        print(f"Hijo con pid {os.getpid()}")
        print(f"Errores encontrados: {contador}\n")
        os._exit(0)

for i in range(3):
    os.wait()#verifica si termina hijo1, luego hijo2 y asi...




