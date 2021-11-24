
class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses is None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already enrolled in the {course} course")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{self.first_name} is not enrolled in the {course} course")

    def __len__(self):
        return len(self.courses)

    def __str__(self):  # __str__ es un metodo que permite retornar directamente todos los datos del objeto (abajo se pone 'print(nombre-obj)', y va a imprimir todos los datos.
        return f"First name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\
        \nCourses: {','.join(map(str.capitalize,self.courses))}"  # map, con el metodo str.capitalize va a hacer que todos los elementos de la lista course empiecen con mayusc.


courses1 = ['python', 'ruby', 'javascript']
courses2 = ['java', 'rails', 'c']

john = Student("john", "wick", courses1)  # john es un objeto de Student. Se puede pensar como una instancia de la clase Student.

paul = Student("paul", "pierce", courses2)

paul.add_course('c++')
john.add_course('c#')
john.remove_course('javascript')
john.remove_course('javascript')

print(john)
print(paul)

  # 'def__init__' es un metodo 'dunder' o 'mágico' sirve para inicializar la instancia de un objeto. Se caracteriza por doble '_'.'Courses' está = 'none' porque sino paso ningun curso va a dar error, y si está en None y paso, no hay problema.
  # 'self' es por convencion el primer parametro que se pasa.Siempre que se use una instanciade la clase se tendrá que usar.
