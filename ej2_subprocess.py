

import subprocess
import urllib


termino = input("Ingrese el termino de busqueda: ")
termino_codificado = urllib.parse.quite(termino) #codifica
url = f"https://www.google.com/search?q={termino_codificado}"

#en LINUX (xdg-open)
try:
    subprocess.run(["xdg-open", url]) # LINUX
except FileNotFoundError:
    try:
        subprocess.run(["open", url]) # macOS
    except FileNotFoundError:
        subprocess.run(["start", url], shell=True) # WINDOWS

print("El navegador se ha abierto en un proceso hijo")