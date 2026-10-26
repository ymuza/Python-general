"""This pattern allows us to create new objects by coping existing objects, without
specifying their concrete classes"""


import copy

class Prototype:
    """Mixin that lets any subclass copy itself."""
    def clone(self):
        """Return a shallow copy of this object."""
        return copy.copy(self)


class Guitar(Prototype):
    """Concrete prototype that can be cloned instead of built from scratch."""
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __str__(self):
        return f'{self.color} {self.model}'


if __name__ == '__main__':
    guitar1 = Guitar('Ibanez', 'red')
    guitar2 = guitar1.clone()

    print(guitar1)
    print(guitar2)
