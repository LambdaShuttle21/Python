import threading
import time

#variable global para guardar areas
areas = []

#en cada def devuelve el area de cada figura (int) agregandola al array
def trianguloEscaleno(base, altura, segundos):
    area = base * altura / 2
    time.sleep(segundos)
    print(f"El area del triangulo escaleno es de: {area}")
    areas.append(area)#no necesito hacer un return porque areas es una variable global que puede ser modificada desde la funcion directamente y como los hilos lanzan las funciones..

def rectanguloArea(base, altura, segundos):
    area = base * altura
    time.sleep(segundos)
    print(f"El area del rectangulo es de: {area}")
    areas.append(area)

def trianguloRectanguloArea(base, altura, segundos):
    area = base * altura / 2
    time.sleep(segundos)
    print(f"El area del triangulo rectangulo es de: {area}")
    areas.append(area)

#hilos
h1 = threading.Thread(target=trianguloEscaleno, args=(10, 12, 2))
h2 = threading.Thread(target=rectanguloArea, args=(8, 12, 3))
h3 = threading.Thread(target=rectanguloArea, args=(6, 5, 4))
h4 = threading.Thread(target=trianguloRectanguloArea, args=(5, 5, 5))
#empiezan casi al mismo tiempo
h1.start()
h2.start()
h3.start()
h4.start()

h1.join()
print("El principal sigue después de h1")

h2.join()
print("El principal sigue después de h2")

h3.join()
print("El principal sigue después de h3")

h4.join()
print("El principal sigue después de h4")

areasTotal = sum(areas)
print(f"El perimetro total es de: {areasTotal}")