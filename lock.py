import threading

#Imagina que todos tus hilos suman a una misma var global
#Sin lock: se pisan todos entre si y el resultado sale mal
#Con lock: garantizas que solo 1 hilo modifique la var a la vez

contador = 0
lock = threading.Lock()

def sumar():
    global contador
    #lo que sucede es simple, ya que todos los hilos intentan modificar contador, es decir, la misma funcion al mismo tiempo, se pisan entre si
    #por ejemplo h1 y h2 entran al mismo tiempo y y leen contador = 0 + 1, es decir, se pierde 1, y contador = 1 luego por ejemplo digamos que 
    #h3 y h4 entran realizando contador += 1 entonces al valer contador = 1 y hacer la misma operacion, se va a perder 1 en el contador y en lugar
    #de valer 4 va a valer 2
    for _ in range(1000):
        with lock:#evita que suceda eso, si 1 hilo entra, los demas ESPERAN Y DESPUES ya modifica la variable el hilo detras en la cola
            contador = contador + 1

#creo 5 hilitos
hilos = []
for i in range(5):
    h = threading.Thread(target=sumar)
    hilos.append(h)

#empieza el circo simultaneo
for h in hilos:
    h.start()
#main thread va esperando h1, h2, h3, h4
for h in hilos:
    h.join()

print("Contador final:", contador)
