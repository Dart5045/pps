# https://docs.python.org/3/library/exceptions.html
# Tenemos que tratar de ser lo más específicos posibles
# Son costosas en rendimiento.
def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por 0", f"{n}")
    return 5/n


try:
    division()
except ZeroDivisionError as e:
    print(e)
