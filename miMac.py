import subprocess


proceso = subprocess.Popen(["ip", "a"], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, text=True )

# con Popen().
# - stdout=subprocess.PIPE → manda la salida normal del comando hacia Python.
# - stderr=subprocess.PIPE → manda los errores hacia Python.
# - text=True → hace que recibas texto normal (str) en vez de bytes.

#de forma no automatica

lineas = list(proceso.stdout)#guardo todas mis lineas en una lista

# .split() divide automaticamente por espacios, 
tarjetaLinea = lineas[6].split()[1].strip(":")
# el [1] en split es: haz el split() y de la lista resultante dame el indice 1
# finalmente el strip(":") quita los ":" de los extremos y queda solo la MAC del pc

macLinea = lineas[7].split()[1]
# aca separamos la linea con .split() sacamos la MAC que seria el indice 1 de la linea 7
print(f"Tarjeta {tarjetaLinea} -> {macLinea}")