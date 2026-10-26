"""Factory pattern: client code asks PersonFactory for a person by type name
instead of instantiating Student or Teacher directly."""

from abc import ABC, abstractmethod


class IPerson(ABC):
    """Interface that every person type created by the factory implements."""

    @abstractmethod
    def person_method(self):
        """interface method"""


class Student(IPerson):
    """Concrete product created by PersonFactory."""
    def __init__(self):
        self.name = "lucas"

    def person_method(self):
        print("i'm a student")


class Teacher(IPerson):
    """Concrete product created by PersonFactory."""
    def __init__(self):
        self.name = "carla"

    def person_method(self):
        print("I'm a teacher")


class PersonFactory:
    """Factory that decides which IPerson subclass to instantiate."""
    @staticmethod
    def build_person(person_type):
        """Return a Student or Teacher for the given type name. Raises ValueError if unknown."""
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        raise ValueError(f"unknown person type: {person_type}")


if __name__ == "__main__":
    s1 = Student()
    s1.person_method()

    s2 = Teacher()
    s2.person_method()

    choice = input("what type of person do you want to create?\n")
    try:
        person = PersonFactory.build_person(choice)
    except ValueError as error:
        print(error)
    else:
        person.person_method()
