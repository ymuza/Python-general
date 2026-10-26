"""Ejemplo de composición: una clase se arma combinando objetos de otras clases
en lugar de heredar de ellas."""

class RoboDog:
    def __init__(self):
        pass

    @staticmethod
    def bark():
        print('woof!')


class RoboCat:
    def __init__(self):
        pass

    @staticmethod
    def meow():
        print('meow')


class Robot:
    def __init__(self):
        pass

    @staticmethod
    def move():
        print('ah...mobility')


class CleanRobot:
    def __init__(self):
        pass

    @staticmethod
    def clean():
        print("I clean ")


# la clase Superbot está compuesta de objetos de las otras clases,
# y puede tener tambien metodos propios
class Superbot:  # esta clase contiene 4 objetos.
    """Robot compuesto que delega cada acción en uno de sus objetos internos."""

    def __init__(self):
        self.o1 = Robot()
        self.o2 = RoboDog()
        self.o3 = RoboCat()
        self.o4 = CleanRobot()

    @staticmethod
    def play_game():
        print("chess is the best!")

    def move(self):
        self.o1.move()

    def bark(self):
        self.o2.bark()

    def meow(self):
        self.o3.meow()

    def clean(self):
        self.o4.clean()


henry = Superbot()  # creo el superbot henry , y abajo le asigno las funciones
henry.move()
henry.clean()
henry.play_game()
