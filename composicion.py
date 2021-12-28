class RoboDog:
    @staticmethod
    def bark():
        print('woof!')


class RoboCat:
    @staticmethod
    def meow():
        print('meow')


class Robot:
    @staticmethod
    def move():
        print('ah...mobility')


class CleanRobot:
    @staticmethod
    def clean():
        print("I clean ")


# la clase Superbot está compuesta de objetos de las otras clases, y puede tener tambien metodos propios
class Superbot:  # esta clase contiene 4 objetos.

    def __init__(self):
        self.o1 = Robot()
        self.o2 = RoboDog()
        self.o3 = RoboCat()
        self.o4 = CleanRobot()

    @staticmethod
    def play_game():
        print("chest is the best!")

    def move(self):
        return self.o1.move()

    def bark(self):
        return self.o2.bark()

    def meow(self):
        return self.o3.meow()

    def clean(self):
        return self.o4.clean()


henry = Superbot()  # creo el superbot henry , y abajo le asigno las funciones
henry.move()
henry.clean()
henry.play_game()
