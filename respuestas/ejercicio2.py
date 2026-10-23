'''
Crea un program en python que haga lo siguiente:
Pregunte por un directorio. Si se quiere listar el directorio actual no se introduce nada
El programa debe reportar cuando el directorio no es correcto por fallo del usuario.
No vale contar ni '.' ni '..' que son el directorio actual y el padre.
'''

import subprocess


directorio = input("Escriba un directorio o pulse ENTER para listar el actual: ")

if directorio == "":
    proceso = subprocess.Popen(["ls", "-a"], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True)
else:
    proceso = subprocess.Popen(["ls", "-a", directorio], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True)

error = False 
for linea in proceso.stderr:
    print(linea.strip())#strip() para eliminar espacios en blanco al inicio y final
    error = True

contador = 0
if not error:
    lista = list(proceso.stdout)
    for fichero in lista[2:]:
        fichero = fichero.strip()
        if fichero[0] == ".":
            print(fichero)
            contador = contador + 1

print(f"Ficheros ocultos: {contador}")


#tambien se puede de esta otra forma

for fichero in lista:
    fichero = fichero.strip()
    if fichero != "." and fichero != "..":
        if fichero[0] == ".":
            print(fichero)   