"""
Las funciones se utilizan en programación para agrupar un conjunto de instrucciones que quieres utilizar repetidamente o que, 
debido a su complejidad, es mejor que estén contenidas en un subprograma y que se invoquen cuando sea necesario
"""


# Imprime un mensaje en la terminal/consola
print("Hola!!!")


def saludo():
    """Empieza palabra reservadad def, seguido con el nombre de la función, además de los parámetros."""
    print("Hola")
    print("dentro de la función")


saludo()


def saludo2(nombre, apellido):
    """Función con parámetros, que tienen sentido en el contexto de la función"""
    print("Hola")
    print(f"Bienvenido {nombre} {apellido}")


saludo2("Juan", "Vargas")  # llamada a la función con argumentos(No parámetros)


def saludo3(nombre, apellido=""):
    """Función con parámetros opcionales, la función cuando no le proporcionemos valor,
      toma el valor por defecto"""
    print("Hola")
    print(f"Bienvenido {nombre} {apellido}")


saludo3("Juan")  # llamada a la función con argumentos(No parámetros)


# Puedes llamar a la función con los argumentos nombrados, es necesario nombrarlos todos
# llamada a la función con argumentos(No parámetros)
saludo3(apellido="Perez", nombre="")
