"""
Las excepciones en Python son una herramienta muy potente que la gran mayoría de lenguajes de programación modernos tienen. 
Se trata de una forma de controlar el comportamiento de un programa cuando se produce un error.
Esto es muy importante ya que salvo que tratemos este error, el programa se parará, y esto es algo que en determinadas aplicaciones no es una opción válida.
"""


try:
    n1 = int(input("Ingresar primer valor numérico: "))
except:
    print("ha ocurrido un error")
