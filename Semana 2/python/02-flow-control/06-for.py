# range es un iterable
for numero in range(5):
    print(numero, numero * "Ups")


# Buscar un número en un rango
buscar = 3
for numero in range(20):
    print(numero)
    if (numero == buscar):
        print("Número encontrado")
        break  # detiene la ejecución de código
else:
    print("Número no encontrado")


# las cadenas tambén son iterables
for char in "Texto de ejemplo":
    print(char)
