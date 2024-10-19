numero1 = input("Introduzca primer número : ")
numero2 = input("Introduzca segundo número : 2")

numero1 = int(numero1)
numero2 = int(numero2)


totalSuma = numero1 + numero2
totalResta = numero1 - numero2
totalMulti = numero1 * numero2
totalDiv = numero1 / numero2

mensaje = f"""
Para los números {numero1} y {numero2},
El resultado de la suma es {totalSuma}
El resultado de la resta es {totalResta}
El resultado de la multiplicacion es {totalMulti}
El resultado de la división es {totalDiv}
"""
print(mensaje)
