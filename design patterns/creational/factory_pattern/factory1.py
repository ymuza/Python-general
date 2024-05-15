import abc
from abc import ABCMeta

class IPerson(metaclass=ABCMeta):

    @abc.abstractmethod
    def person_method(self):
        """interface method"""

class Student(IPerson):
    def __int__(self):
        self.name = "lucas"

    def person_method(self):
        print("i'm a student")

class Teacher(IPerson):
    def __int__(self):
        self.name = "carla"

    def person_method(self):
        print("I'm a teacher")


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("invalid type")
        return -1

if __name__ == "__main__":
    choice = input("what type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()







s1 = Student()
s1.person_method()

s2 = Teacher()
s2.person_method()




# p1 = IPerson()
# p1.person_method()




