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
