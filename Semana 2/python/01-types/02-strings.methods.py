"""
Métodos sobre cadenas
"""
nombre_curso = " utlimATe pytHOn course"

# Todo a mayúscula
print(nombre_curso.upper())
# Todo a minúscula
print(nombre_curso.lower())

# Mayúscula primer caracter, todo lo demás a minúscula
print(nombre_curso.capitalize())

# Mayúscula la primera letra de cada palabra, lo demás a minúscula
print(nombre_curso.title())

# Remueve espacios en blanco a la derecha e izquierda
print(nombre_curso.strip())

# Se puede encadenar métodos
print(nombre_curso.strip().capitalize())

# Elimina espacios a la derecha
print(nombre_curso.rstrip())

# Elimina espacios a la izquierda
print(nombre_curso.lstrip())

# Buscar una cadena en una cadena que se encuentra en un string
print(nombre_curso.find("HO"))

# Buscar una cadena en una cadena que no se encuentra en un string
print(nombre_curso.find("HOLA"))

# Case sensitive, remplaza una cadena de caracteres, si la encuentra
print(nombre_curso.replace("HO", "ho"))

# find encuentra el indice, este método devuelve un booleano si encuentra el/los caracteres en una variable
print("HO" in nombre_curso)

# find encuentra el indice, este método devuelve un booleano si NO encuentra el/los caracteres en una variable
print("HOLA" not in nombre_curso)
