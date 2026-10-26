"""Shows the __init__ constructor and the difference between class and instance variables."""

class Person:
    """A person with a name and age; species is shared by every instance."""

    species = "human"  # class variable shared by all instances

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    def is_adult(self):
        """Prints whether the person is older than 20."""
        if self.age > 20:
            print(f"{self.name} is an adult")
        else:
            print(f"{self.name} is not an adult")

    def which_species(self):
        print(f"{self.name} is from the {self.species} species ")


p1 = Person('charles', 10)  # p1 is an object from the class Person
p1.is_adult()
p1.which_species()

p2 = Person('karen', 21)
p2.is_adult()
p2.which_species()
