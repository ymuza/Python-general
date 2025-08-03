


class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []
        self.cheese = None

    def __str__(self):
        return f"{self.size} {self.crust} pizza with {self.cheese} cheese and toppings: {', '.join(self.toppings)}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def size(self, size):
        self.pizza.size = size
        return self  # Return self to enable method chaining

    def crust(self, crust):
        self.pizza.crust = crust
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def build(self):
        return self.pizza


# Usage examples:
builder = PizzaBuilder()

# Build a simple pizza
pizza1 = (builder
          .size("Large")
          .crust("Thin")
          .cheese("Mozzarella")
          .add_topping("Pepperoni")
          .build())

# Build a different pizza with the same builder
builder2 = PizzaBuilder()
pizza2 = (builder2
          .size("Medium")
          .crust("Thick")
          .cheese("Cheddar")
          .add_topping("Mushrooms")
          .add_topping("Bell Peppers")
          .add_topping("Olives")
          .build())

print(pizza1)
print(pizza2)