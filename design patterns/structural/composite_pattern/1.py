
"""Composite pattern composes objects in terms of a tree structure to represent part as well as whole hierarchy.
This type of design pattern comes under structural pattern as this pattern creates a tree structure of group of objects.
 This pattern creates a class that contains group of its own objects.

The springfield power plant has two important divisions, the Management, run by mr Burns, and
the 7-G sector, which main asset is homer. The class Components is the root branch, and
  manages the leafs, which would be in this case the divisions. """


class Components:
    def __init__(self, name):
        self.name = name

    def add(self, components):
        pass

    def delete(self, components):
        pass

    def show(self, level):
        pass


class Department(Components):
    def __init__(self, name):
        super().__init__(name)
        self.components = []

    def add(self, components):
        self.components.append(components)

    def delete(self, components):
        self.components.remove(components)

    def show(self, level):
        print(f"{' ' * level}{self.name}")
        for components in self.components:
            components.show(level + 2)


class Employees(Components):
    def show(self, level):
        print(f"{' ' * level}{self.name}")


if __name__ == '__main__':
    company = Department("Springfield Nuclear Power Plant")

    Department1 = Department("Sector 7-G")
    Department2 = Department("Management")

    employee1 = Employees("Homer Simpson")
    employee2 = Employees("Lenny Leonard")
    employee3 = Employees("Carl Carlson")
    employee4 = Employees("Waylon Smithers, Jr.")
    employee5 = Employees("Charles Montgomery Burns")

    Department1.add(employee1)
    Department1.add(employee2)
    Department1.add(employee3)
    Department2.add(employee4)
    Department2.add(employee5)
    company.add(Department1)
    company.add(Department2)

    company.show(0)
