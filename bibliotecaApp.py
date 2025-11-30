
# listado general 30 libros
biblioteca_general = [
    {"titulo": "El Hobbit", "autor": "Tolkien", "paginas": 300, "genero": "Fantasía"},
    {"titulo": "1984", "autor": "Orwell", "paginas": 250, "genero": "Distopía"},
    {"titulo": "Dune", "autor": "Herbert", "paginas": 500, "genero": "Ciencia ficción"},
    {"titulo": "It", "autor": "Stephen King", "paginas": 600, "genero": "Terror"},
    {"titulo": "Fundación", "autor": "Asimov", "paginas": 230, "genero": "Ciencia ficción"},
    {"titulo": "Neuromante", "autor": "William Gibson", "paginas": 280, "genero": "Ciencia ficción"},
    {"titulo": "El Juego de Ender", "autor": "Orson Scott Card", "paginas": 320, "genero": "Ciencia ficción"},
    {"titulo": "La Llamada de Cthulhu", "autor": "H.P. Lovecraft", "paginas": 140, "genero": "Terror"},
    {"titulo": "Drácula", "autor": "Bram Stoker", "paginas": 400, "genero": "Terror"},
    {"titulo": "Frankenstein", "autor": "Mary Shelley", "paginas": 230, "genero": "Terror"},
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "paginas": 100, "genero": "Fábula"},
    {"titulo": "Crimen y castigo", "autor": "Dostoievski", "paginas": 430, "genero": "Drama"},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "paginas": 600, "genero": "Novela"},
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "paginas": 470, "genero": "Realismo mágico"},
    {"titulo": "Don Quijote", "autor": "Cervantes", "paginas": 1000, "genero": "Clásico"},
    {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón", "paginas": 520, "genero": "Misterio"},
    {"titulo": "El Código Da Vinci", "autor": "Dan Brown", "paginas": 450, "genero": "Thriller"},
    {"titulo": "Los Juegos del Hambre", "autor": "Suzanne Collins", "paginas": 370, "genero": "Distopía"},
    {"titulo": "Harry Potter 1", "autor": "J.K. Rowling", "paginas": 350, "genero": "Fantasía"},
    {"titulo": "Harry Potter 2", "autor": "J.K. Rowling", "paginas": 370, "genero": "Fantasía"},
    {"titulo": "Harry Potter 3", "autor": "J.K. Rowling", "paginas": 430, "genero": "Fantasía"},
    {"titulo": "La Metamorfosis", "autor": "Kafka", "paginas": 120, "genero": "Absurdismo"},
    {"titulo": "El Nombre del Viento", "autor": "Patrick Rothfuss", "paginas": 700, "genero": "Fantasía"},
    {"titulo": "El Temor de un Hombre Sabio", "autor": "Patrick Rothfuss", "paginas": 1100, "genero": "Fantasía"},
    {"titulo": "El Señor de los Anillos 1", "autor": "Tolkien", "paginas": 500, "genero": "Fantasía"},
    {"titulo": "El Señor de los Anillos 2", "autor": "Tolkien", "paginas": 450, "genero": "Fantasía"},
    {"titulo": "El Señor de los Anillos 3", "autor": "Tolkien", "paginas": 550, "genero": "Fantasía"},
    {"titulo": "Solaris", "autor": "Stanislaw Lem", "paginas": 300, "genero": "Ciencia ficción"},
    {"titulo": "El Perfume", "autor": "Patrick Süskind", "paginas": 280, "genero": "Drama"},
    {"titulo": "El Alquimista", "autor": "Paulo Coelho", "paginas": 210, "genero": "Fábula"}
]


# ============================================
#   PLANTILLA DE PRUEBA OBSERVACIÓN DIRECTA – GESTIÓN BIBLIOTECA
# ============================================


# --- EJERCICIO 1 ---
def crear_libro(titulo: str, autor: str, paginas: int, genero: str):
    """
    TODO: devolver un diccionario con los datos del libro.
    """
    libro = {"titulo": titulo, "autor": autor, "paginas": paginas, "genero": None}
    if (genero != None):
        libro["genero"] = genero
    else:
        print("genero por defecto none")
    return libro

#libros
libro1 = crear_libro(
    "Heredero del Imperio (Heir to the Empire)",
    "Timothy Zahn",
    470,
    genero="Space Opera / Leyendas"
)

libro2 = crear_libro(
    "Perdido (Lost Stars)",
    "Claudia Gray",
    551,
    genero="Juvenil / Aventura"
)

libro3 = crear_libro(
    "Light of the Jedi",
    "Charles Soule",
    400,
    genero="Alta República / Aventura"
)

libro4 = crear_libro(
    "Darth Bane: Path of Destruction",
    "Drew Karpyshyn",
    346,
    genero="Fantasía Oscura / Sith"
)

libro5 = crear_libro(
    "Catalyst: A Rogue One Novel",
    "James Luceno",
    400,
    genero="Espionaje / Precuela"
)
libro6 = crear_libro("Kenobi", "John Jackson Miller", 416, genero="Aventura / Jedi")
libro7 = crear_libro("The Weapon of a Jedi", "Jason Fry", 240, genero="Juvenil / Luke Skywalker")
libro8 = crear_libro("Leia: Princess of Alderaan", "Claudia Gray", 409, genero="Juvenil / Princesa")
libro9 = crear_libro("Ahsoka", "E.K. Johnston", 400, genero="Juvenil / Aventura")


# --- EJERCICIO 2 ---
# Ejercicio 2 – Búsqueda dentro de una biblioteca (2 puntos)
# Objetivo: trabajar filtrado, funciones y métodos .get().
# 1. (0,5 puntos) Crea una función buscar_por_autor(biblio, autor) que
# devuelva una lista con todos los libros escritos por ese autor.
# 2. (0,5 puntos) Haz que la función use .get() para evitar errores cuando
# falte algún campo.
# 3. (0,5 puntos) Prueba la función con biblioteca1 e imprime los
# resultados.
# 4. (0,5 puntos) Si no encuentra ningún libro, devuelve el mensaje
# "Autor no encontrado".
#le paso el tipo de dato a mis args
def buscar_por_autor(biblio: List[Dict[str, Any]], autor: str) -> List[Dict[str, Any]]:
    resultado: List[Dict[str, Any]] = []
    #recorro mi lista de diccionarios, la var libro es un Dict
    for libro in biblio:
        # recorro mi diccionario con el .items() que me devuelve una tupla clave-valor, recorre el diccionario 4 veces ya que tengo 4 clave-valor
        for clave, valor in libro.items():
            print(f"{clave}: {valor}")
        # si el autor pasado como args existe en algun libro (value de mi key "autor"), se agrega a mi nueva lista de diccionarios "resultado"
        if libro["autor"] == autor:
            resultado.append(libro)
    return resultado



# --- EJERCICIO 3 ---
"""
Ejercicio 3 – Diccionarios dentro de diccionarios (2 puntos)
Objetivo: construir estructuras anidadas más complejas.
1. (0,5 puntos) Crea un diccionario biblioteca_detallada donde cada
clave sea el título del libro y cada valor sea un diccionario interno con
autor, páginas y género.
2. (0,5 puntos) Añade un subdiccionario adicional llamado "prestamo"
con información como:
"prestamo": {"disponible": True, "dias_restantes": 0}
3. (0,5 puntos) Crea una función info_libro(diccionario, titulo) que
imprima toda la información del libro incluyendo los datos del préstamo.
4. (0,5 puntos) Si el título no existe, muestra el mensaje "El libro no está
en la biblioteca". """

#biblioteca detallada
biblioteca_dict = {
    libro1["titulo"]: libro1,
    libro2["titulo"]: libro2,
    libro3["titulo"]: libro3,
    libro4["titulo"]: libro4,
    libro5["titulo"]: libro5
}

from typing import Dict, Any, List

def info_libro(biblioteca: Dict[str, Dict[str, Any]], titulo: str) -> None:
    """
    Imprime toda la información de un libro dentro de un diccionario de diccionarios.
    Si no existe, muestra mensaje adecuado.
    """
    #SI LO QUE TE DOY COMO ARGS (titulo) EXISTE COMO CLAVE EN biblioteca, entonces...
    if titulo in biblioteca:
        libro = biblioteca[titulo]#Me devuelve el diccionario que pertenece a la clave, es decir al titulo
        #una vez tenga el valor (el diccionario) lo recorro
        print("Informacion del libro: ")
        for clave, valor in libro.items():
            print(f"{clave}: {valor}")
    else:
        print(f"No se encontró el libro con título: {titulo}")



# Ejercicio 4 – Múltiples bibliotecas (2 puntos)
# Objetivo: manejar una estructura de diccionarios dentro de diccionarios,
# basada en las técnicas vistas en el documento (anidamiento).
# 1. (0,5 puntos) Crea tres bibliotecas llamadas biblioteca1, biblioteca2
# y biblioteca3, cada una con al menos 3 libros.
# 2. (0,5 puntos) Crea un diccionario general llamado sistema_bibliotecas
# con esta estructura:
# {
# "central": biblioteca1,
# "universitaria": biblioteca2,
# "infantil": biblioteca3
# }
# 3. (0,5 puntos) Recorre todas las bibliotecas usando items() e imprime la
# cantidad de libros de cada una (usa len()).
# 4. (0,5 puntos) Añade al sistema una nueva biblioteca vacía llamada
# "digital".
# --- EJERCICIO 4 ---

sistema = {}
def crear_sistema_bibliotecas():

    biblioteca1 = {libro1["titulo"]: libro1, libro2["titulo"]: libro2, libro3["titulo"]: libro3}
    biblioteca2 = {libro4["titulo"]: libro4, libro5["titulo"]: libro5, libro6["titulo"]: libro6}
    biblioteca3 = {libro7["titulo"]: libro7, libro8["titulo"]: libro8, libro9["titulo"]: libro9}
    bibliotecaDigital = {}

    sistema = {"central": biblioteca1, "universitaria": biblioteca2, "infantil": biblioteca3, "digital": bibliotecaDigital}
    #darme el valor asociado a la clave de sistema
    biblioCentral = sistema["central"]
    biblioUniversitaria = sistema["universitaria"]
    biblioInfantil = sistema["infantil"]
    #cantidad libros
    biblioCentralCantidad = len(biblioCentral)
    biblioUniversitariaCantidad = len(biblioUniversitaria)
    biblioInfantilCantidad = len(biblioInfantil)
    #recorro todas las bibliotecas, me dan k-v y con el value que me da
    for nombre, biblioteca in sistema.items():
        print(f"Mostrando biblioteca {nombre}:")
        #recorro mi value biblioteca que dentro tendra otra tupla k-v donde el valor me va a devolver directamente el libro (Dict)
        for titulo, datos in biblioteca.items():
            print(f"{titulo}: {datos}")
    print(f"Cantidad de libros de biblioteca central: {biblioCentralCantidad}")
    print(f"Cantidad de libros de biblioteca universitaria: {biblioUniversitariaCantidad}")
    print(f"Cantidad de libros de biblioteca infantil: {biblioInfantilCantidad}")
    return sistema
    
resSistema = crear_sistema_bibliotecas()  

# --- EJERCICIO 5 ---
def buscar_libro_global(sistema, titulo):
    """
    TODO: buscar un libro en todas las bibliotecas del sistema.
    """
    for nombreBiblioteca, biblioteca in sistema.items():
        for libroTitulo, libro in biblioteca.items():
            if libroTitulo == titulo:
                return titulo, nombreBiblioteca


def buscar_autor_global(sistema, autor):
    """
    TODO: devolver todos los libros de un autor en todas las bibliotecas.
    """
    res = []
    for nombreBiblioteca, biblioteca in sistema.items():
        for libroTitulo, libro in biblioteca.items():
            for libroAutor, info in libro.items():
                if libroAutor["autor"] == autor:
                    res.append(libro)
    return res                 


# ============================================
#          MENÚ PRINCIPAL DEL EXAMEN
# ============================================

def menu_principal():
    
    while True:
        print("\n===== GESTIÓN DE BIBLIOTECA =====")
        print("1. Crear libro")
        print("2. Buscar libros por autor")
        print("3. Mostrar información detallada de un libro")
        print("4. Crear sistema de bibliotecas")
        print("5. Buscar libro en todas las bibliotecas")
        print("6. Buscar autor en todas las bibliotecas")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("OPCIÓN 1: Crear libro")
            # TODO: pedir datos al usuario y llamar a crear_libro()

        elif opcion == "2":
            print("OPCIÓN 2: Buscar libros por autor")
            # TODO:

        elif opcion == "3":
            print("OPCIÓN 3: Información detallada de libro")
            # TODO: 

        elif opcion == "4":
            print("OPCIÓN 4: Crear sistema de bibliotecas")
            # TODO: 

        elif opcion == "5":
            print("OPCIÓN 5: Búsqueda global de libro")
            # TODO

        elif opcion == "6":
            print("OPCIÓN 6: Búsqueda global de autor")
            # TODO

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# EJECUTAR MENÚ
menu_principal()
