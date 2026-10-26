"""Bridge pattern: decouples an abstraction from its implementation so both can vary
independently. Here the abstraction is the Vehicle hierarchy (Car, Truck) and the
implementation is the Renderer hierarchy (RedRenderer, BlueRenderer). A Vehicle holds
a Renderer instead of inheriting from it, so any vehicle can be drawn in any color."""

from abc import ABC, abstractmethod


class Renderer(ABC):
    """Implementor: knows how to render a shape in a given color."""
    @abstractmethod
    def render(self, shape: str) -> str:
        """Return a description of the shape drawn in this renderer's color."""


class RedRenderer(Renderer):
    """Concrete implementor that renders in red."""
    def render(self, shape):
        return f"Drawing a red {shape}"


class BlueRenderer(Renderer):
    """Concrete implementor that renders in blue."""
    def render(self, shape):
        return f"Drawing a blue {shape}"


class Vehicle(ABC):
    """Abstraction: a vehicle that delegates its drawing to a Renderer."""
    def __init__(self, renderer: Renderer):
        self._renderer = renderer

    @abstractmethod
    def draw(self) -> str:
        """Return a description of the drawing. Subclasses implement it."""


class Car(Vehicle):
    """Refined abstraction: a car."""
    def draw(self):
        return self._renderer.render("car")


class Truck(Vehicle):
    """Refined abstraction: a truck."""
    def draw(self):
        return self._renderer.render("truck")


if __name__ == "__main__":
    red_car = Car(RedRenderer())
    print(red_car.draw())

    blue_truck = Truck(BlueRenderer())
    print(blue_truck.draw())

    blue_car = Car(BlueRenderer())
    print(blue_car.draw())
