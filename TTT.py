class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mayor_edad(self):
        if self.edad > 18:
            return True
        else:
            return False


p = Persona('luis', 45)

p.mayor_edad()
