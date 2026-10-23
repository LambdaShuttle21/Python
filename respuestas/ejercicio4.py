'''
    Escribe un programa en Python, ejer4.py, que:
    ◦ Usa el comando de linux md5sum que saca el hash de un archivo. El hash es un número único que si el archivo no cambia es siempre igual. Cualquier cambio provocará un  cambio en el número. 
    ◦ Pide una cadena de texto, le realiza el md5sum, usando subprocess.Popen y lo muestra por pantalla.
    ◦ El programa sigue pidiendo una nueva frase y realizando lo dicho en el segundo punto hasta que se para con la cadena ‘salir’.
'''
import subprocess

entrada = input("Escribe la frase('salir' para acabar): ")

while entrada != "salir":
    #abrimos proceso.
    proceso = subprocess.Popen(
        ["md5sum"], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE,
        text=True
    )
    proceso.stdin.write(entrada)
    proceso.stdin.flush()
    # Cerramos stdin para indicar que no enviaremos más
    proceso.stdin.close()
    # Leemos la salida
    salida = proceso.stdout.read()
    print("=== SALIDA ===")
    print(salida)

    #volvemos a preguntar.
    entrada = input("Escribe la frase(salir para acabar): ")
