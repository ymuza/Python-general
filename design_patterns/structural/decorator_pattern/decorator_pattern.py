"""This pattern allows us to add new behavior to an object by wrapping it with one or more
 decorator objects. This pattern is useful when you want to add functionality to an object
  dynamically, without changing its source code. """


class Component:
    """Interface shared by the real component and its decorators."""
    def operation(self):
        pass


class ConcreteComponent(Component):
    """The base object that decorators wrap."""
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    """Base decorator: wraps a component and delegates operation() to it."""
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """Decorator that wraps the inner result in 'ConcreteDecoratorA(...)'."""
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    """Decorator that wraps the inner result in 'ConcreteDecoratorB(...)'."""
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"


if __name__ == '__main__':
    base_component = ConcreteComponent()
    decorator1 = ConcreteDecoratorA(base_component)
    decorator2 = ConcreteDecoratorB(decorator1)

    print(decorator2.operation())  # "ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))"
