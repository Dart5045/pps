# Estoy capturando todos los errores
# try:
#     n1 = int(input("Ingresar primer valor numérico: "))
# except Exception as e:
#     print(type(e))


try:
    n1 = int(input("Ingresar primer valor numérico: "))
    adfas
except ValueError as e:
    print("Ingrese un valor que corresponda")
except NameError as e:
    print("Ocurrió un error inesperado")
else:  # Bloque que se ejecuta si no ha ocurrido un error
    print("No ocurrió ningún error")
finally:  # Bloque que se ejecuta siempre
    print("Se ejecuta siempre!")
