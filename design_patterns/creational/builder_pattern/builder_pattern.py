"""Builder pattern: separates the construction of a complex object from its
representation. Here PizzaBuilder assembles a Pizza one topping at a time
through chained method calls, and build() returns the finished product."""

class Pizza:
    """The product being built. It starts empty and the builder fills it in."""
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.olives = False

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("cheese")
        if self.pepperoni:
            toppings.append("pepperoni")
        if self.mushrooms:
            toppings.append("mushrooms")
        if self.olives:
            toppings.append("olives")

        if not toppings:
            return f"{self.size} pizza"
        return f"{self.size} pizza with {', '.join(toppings)}"


class PizzaBuilder:
    """Builds a Pizza step by step. Every step returns self so calls can be chained."""
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        """Set the pizza size, e.g. 'large'."""
        self.pizza.size = size
        return self  # Return self for method chaining

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_olives(self):
        self.pizza.olives = True
        return self

    def build(self):
        """Return the finished pizza and reset the builder for the next one."""
        pizza = self.pizza
        self.pizza = Pizza()
        return pizza


if __name__ == "__main__":
    builder = PizzaBuilder()

    pizza = (builder
             .set_size("large")
             .add_cheese()
             .add_pepperoni()
             .add_mushrooms()
             .build())
    print(pizza)  # Output: large pizza with cheese, pepperoni, mushrooms

    plain = builder.set_size("small").build()
    print(plain)  # Output: small pizza
