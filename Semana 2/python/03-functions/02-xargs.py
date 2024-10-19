"""
El principal uso de *args y **kwargs es en la definición de funciones. Ambos permiten pasar un número variable de argumentos a una función, 
por lo que si quieres definir una función cuyo número de parámetros de entrada puede ser variable, considera el uso de *args o **kwargs como una opción.
"""

def suma(x, y):
    """ Función clásica con 2 parámetros """
    print(x+y)


def sumaXargs(*numeros):
    """Al agregar el asterísco al inicio de la función, le decimos que esa variable es iterable"""
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


sumaXargs(1, 2, 3)
