"""Composite pattern composes objects in terms of a tree structure to represent part
as well as whole hierarchy. This type of design pattern comes under structural pattern
as this pattern creates a tree structure of group of objects.
 This pattern creates a class that contains group of its own objects.

The springfield power plant has two important divisions, the Management, run by mr Burns, and
the 7-G sector, which main asset is homer. Components is the common interface; Department
is the composite that contains other components (sub-departments or employees), and
Employees are the leaves."""


class Components:
    """Common interface shared by leaves (Employees) and composites (Department)."""
    def __init__(self, name):
        self.name = name

    def add(self, components):
        """Add a child component. Only composites support it."""
        raise NotImplementedError("leaves cannot contain components")

    def delete(self, components):
        """Remove a child component. Only composites support it."""
        raise NotImplementedError("leaves cannot contain components")

    def show(self, level):
        """Print this component indented by level spaces."""


class Department(Components):
    """Composite: holds child components and shows them recursively."""
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
    """Leaf: a single employee with no children."""
    def show(self, level):
        print(f"{' ' * level}{self.name}")


if __name__ == '__main__':
    company = Department("Springfield Nuclear Power Plant")

    sector_7g = Department("Sector 7-G")
    management = Department("Management")

    employee1 = Employees("Homer Simpson")
    employee2 = Employees("Lenny Leonard")
    employee3 = Employees("Carl Carlson")
    employee4 = Employees("Waylon Smithers, Jr.")
    employee5 = Employees("Charles Montgomery Burns")

    sector_7g.add(employee1)
    sector_7g.add(employee2)
    sector_7g.add(employee3)
    management.add(employee4)
    management.add(employee5)
    company.add(sector_7g)
    company.add(management)

    company.show(0)
