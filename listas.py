from pyparsing import nums

nums = [10, 20, 30, 40, 50]#inclusivo (inicio) exclusivo (fin)
print(nums[1:4])   # [20, 30, 40]

#lista[inicio:fin:paso]

print(nums[:3])    # [10, 20, 30]   (desde el inicio hasta antes del índice 3)
print(nums[2:])    # [30, 40, 50]   (desde índice 2 hasta el final)

print(nums[::2])   # [10, 30, 50]   (de 2 en 2)
print(nums[1::2])  # [20, 40]       (empezando en índice 1, de 2 en 2)

print(nums[::-1])  # [50, 40, 30, 20, 10]

print(nums[-3:])   # [30, 40, 50]   (los últimos 3 elementos)
print(nums[:-2])   # [10, 20, 30]   (todos menos los últimos 2)

copia = nums[:]    # [10, 20, 30, 40, 50] copia la lista entera

#metodos de listas

# ================================
# Chuletario de métodos de listas
# ================================

# Lista de ejemplo
nums = [10, 20, 30, 40]

print("Lista inicial:", nums)

# --- Agregar elementos ---
nums.append(50)              # Agrega al final
print("append:", nums)

nums.insert(1, 15)           # Inserta en posición 1
print("insert:", nums)

nums.extend([60, 70])        # Agrega varios elementos
print("extend:", nums)

# --- Eliminar elementos ---
nums.remove(20)              # Elimina la primera aparición de 20
print("remove:", nums)

valor = nums.pop()           # Elimina el último y lo devuelve
print("pop:", nums, "valor eliminado:", valor)

nums.clear()                 # Vacía la lista
print("clear:", nums)

# --- Reiniciamos lista ---
nums = [10, 20, 30, 40, 30]

# --- Búsqueda y conteo ---
print("index(30):", nums.index(30))   # Primer índice de 30
print("count(30):", nums.count(30))   # Cuántas veces aparece 30

# --- Ordenar y modificar ---
nums.sort()                  # Orden ascendente
print("sort:", nums)

nums.sort(reverse=True)      # Orden descendente
print("sort reverse:", nums)

nums.reverse()               # Invierte el orden
print("reverse:", nums)

# --- Copiar ---
copia = nums.copy()
print("copy:", copia)

# --- Slicing (bonus) ---
print("slice [1:4]:", nums[1:4])      # Del índice 1 al 3
print("slice [::2]:", nums[::2])      # De 2 en 2
print("slice[::-1]:", nums[::-1])     # Invertida

