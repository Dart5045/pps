import math

# Documentación oficial: https://docs.python.org/3/library/math.html

# Redondeo
print(round(1.3))
print(round(1.7))
print(round(1.5))

# Valor absoluto, saca el signo
print(abs(-55))


# Python no trae muchas funciones matemáticas nativas, pero tiene un módulo llamada math

# Número entero más cercano hacia arriba
print(math.ceil(1.1))

# Número entero más cercano hacia abajo
print(math.floor(1.1))

# Valida si lo que le estamos pasando no es un númoer
print(math.isnan(23.3))
# print(math.isnan("texto"))

# Eleva un número a una potencia X
print(math.pow(10, 3))

# Raiz cuadrada de un número
print(math.sqrt(4))
