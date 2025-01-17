class Humano():  # Creamos la clase Humano
    # Definimos el parámetro edad , nombre y ocupación
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad  # Definimos que el atributo edad, sera la edad asignada
        self.nombre = nombre  # Definimos que el atributo nombre, sera el nombre asig
        self.ocupacion = ocupacion  # DEFINIMOS EL ATRIBUTO DE INSTANCIA OCUPACIÓN

    # Creación de un nuevo método
    def presentar(self):
        presentacion = (
            "Hola soy {}, mi edad es {} y mi ocupación es {}")  # Mensaje
        print(presentacion.format(self.nombre, self.edad,
              self.ocupacion))  # Usamos FORMAT

    # Creamos un nuevo método para cambiar la ocupación:
    # En caso que esta persona sea contratada
    def contratar(self, puesto):  # añadimos un nuevo parámetro en el método
        self.puesto = puesto
        print("{} ha sido contratado como {}".format(self.nombre, self.puesto))
        self.ocupacion = puesto  # Ahora cambiamos el atributo ocupación


Persona1 = Humano(31, "Pedro", "Desocupado")  # Instancia
Persona1.presentar()
print(isinstance(Persona1, Humano))
