from abc import ABC, abstractmethod

# Abstraction and Encapsulation
class Animal(ABC):
    def __init__(self, name):
        self._name = name  # Encapsulated with underscore (convention for "protected")

    @abstractmethod
    def make_sound(self):
        pass  # Abstract method – forces child classes to implement this

    def get_name(self):
        return self._name  # Encapsulation – controlled access

# Inheritance
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Inheriting constructor
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self._name} is fetching!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        return "Meow!"

    def climb(self):
        return f"{self._name} is climbing!"

# Polymorphism – same method called on different objects
def animal_speak(animal: Animal):
    print(f"{animal.get_name()} says: {animal.make_sound()}")

# Usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Gray")

animal_speak(dog)   # Polymorphism in action
animal_speak(cat)   # Same interface, different implementation

print(dog.fetch())  # Dog-specific method
print(cat.climb())  # Cat-specific method
