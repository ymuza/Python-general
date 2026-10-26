"""This pattern allow us to define a template for a group of methods, without their
implementation. Its useful when you want to define a set of methods that must be implemented
by a subclass, without explaining how they should be implemented"""


import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print('Woof!')


class Cat(Animal):
    def make_sound(self):
        print('Meow!')


if __name__ == '__main__':
    dog = Dog()
    cat = Cat()

    dog.make_sound()
    cat.make_sound()


