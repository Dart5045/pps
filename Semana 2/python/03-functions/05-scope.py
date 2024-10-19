# El alcance de una variable sólo existe para ese contexto.
# Para que exista una variable en todo el contexto, hay que definirla de forma global
# El uso de variables globales es mala practica.
saludo_str = "Hola global"


def saludo():
    global saludo_str
    saludo_str = "Hola"
    print(saludo_str)


def saludoMario():
    saludo_str = "Hola Mario"
    print(saludo_str)


saludo()
saludoMario()
print(saludo_str)


# Error que podría causar este uso
saludo_str = 2
saludo()
resultadoX = saludo_str+3
print(resultadoX)
