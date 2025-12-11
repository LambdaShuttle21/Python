import threading, time

#Los hilos son programas simultaneos que funcionan de forma pararela dentro de un progrma principal

#El .join() no congela a todos los hilos, solo al hilo que lo llama. Normalmente es el hilo principal (tu script).

def tarea(nombre, segundos):
    print(f"⏳ {nombre} empieza")
    time.sleep(segundos)#metodo de delay segun n segundos
    print(f"✅ {nombre} termina")

h1 = threading.Thread(target=tarea, args=("Hilo 1", 3))
h2 = threading.Thread(target=tarea, args=("Hilo 2", 5))

h1.start()#inicia la actividad del hilo (la funcion tarea)
h2.start()

h1.join()   # El principal espera SOLO a h1
print("🚀 El principal sigue después de h1")

h2.join()   # Ahora espera SOLO a h2
print("🏁 El principal sigue después de h2")

