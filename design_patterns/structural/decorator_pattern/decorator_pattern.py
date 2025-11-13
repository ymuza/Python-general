"""This pattern allows us to add new behavior to an object by wrapping it with one or more
 decorator objects. This pattern is useful when you want to add functionality to an object
  dynamically, without changing its source code. """


class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"


if __name__ == '__main__':
    component = ConcreteComponent()
    decorator1 = ConcreteDecoratorA(component)
    decorator2 = ConcreteDecoratorB(decorator1)

    print(decorator2.operation())  # "ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent))"
