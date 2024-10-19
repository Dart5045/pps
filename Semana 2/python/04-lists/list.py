""" Crear una lista en Python es muy simple, y gracias que cuenta con dos alternativas para hacerlo, tenemos mucho más control sobre cómo y dónde es posible generar y gestionar una lista. 
El primer método para crear una lista en Python es utilizando la notación de corchetes [ ]
"""
numeros = [1, 2, 3, 3]
letras = ["A", "B", "C"]
palabras = ["Hola", "Mundo"]
booleans = [True, False, True]

listado_repetido = [1, 4] * 5

matriz = [[1, 0], [2, 1], [4, 5]]
concatenar_listas = numeros+letras
rango = list(range(1, 11))
chars = list("Hola Mundo")

print(listado_repetido)
print(concatenar_listas)
print(rango)
print(chars)
