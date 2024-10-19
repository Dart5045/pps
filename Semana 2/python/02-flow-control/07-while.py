# duplicar el número hasta que sea igual o mayour a 100
numero = 1
while numero < 100:  # criterio de evaluación, si es cierto ejecuta el bloque
    print(numero)
    numero *= 2


# Emular la línea de comenados de la terminal
comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)


# Bucle infinito

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
