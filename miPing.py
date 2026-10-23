# Lanzamos el comando ping
import subprocess


proceso = subprocess.Popen(
    ["ping", "-c", "5", "google.com"],
    # -c 5 = hacer 5 pings (Linux/Mac)
    stdout=subprocess.PIPE,  # Envía la salida hacia Python
    stderr=subprocess.PIPE,  # Envía la salida de error hacia Python
    text=True  # Convierte la salida a texto en vez de bytes
)

print("Haciendo un ping en tiempo real...\n")

for linea in proceso.stdout:
    if "ttl" in linea:
        mi_lista = linea.split()#divido mi linea en array
        ip = mi_lista[4]#busco la IP y guardo
        #formateo e imprimo
        print(f"El servidor {ip[:-1]} nos envia los datos : {linea.split(":", 1)[1].strip()}")
        #(":", 1) dentro de split significa divide por los 2 puntos 1 sola vez, luego el [1]
        #significa agarra solo la 2da parte de la lista de 2 partes que nos devuelve,
        #sino pusiesemos el numero en el constructor la corta en todos los 2 puntos
        #split: divide segun el delimitador entre parentesis
        #strip: borra espacios vacios o caracteres especificos del inicio y del final de un texto
        