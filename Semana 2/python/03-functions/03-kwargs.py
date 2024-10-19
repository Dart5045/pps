def traer_elemento(**datos):
    # KeyWord Arguments
    print(datos["id"], datos["nombre"])


# Cada vez que llame a una funcion que usa KeyWord Argumentos, tengo que indicar el nombre del parámtro.
# El resultado es un diccionario
traer_elemento(id="23", nombre="Samsung", desc="Teléfono movil")
