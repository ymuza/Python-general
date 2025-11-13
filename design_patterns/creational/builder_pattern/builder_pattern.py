class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.olives = False

    def __str__(self):
        toppings = []
        if self.cheese: toppings.append("cheese")
        if self.pepperoni: toppings.append("pepperoni")
        if self.mushrooms: toppings.append("mushrooms")
        if self.olives: toppings.append("olives")

        return f"{self.size} pizza with {', '.join(toppings)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
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
        return self.pizza


# Usage
pizza = (PizzaBuilder()
         .set_size("large")
         .add_cheese()
         .add_pepperoni()
         .add_mushrooms()
         .build())

print(pizza)  # Output: large pizza with cheese, pepperoni, mushrooms