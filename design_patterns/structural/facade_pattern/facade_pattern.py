"""This pattern allows us to create a simplified interface to a complex system of classes,
making it easier to use and reducing the overall complexity of the code."""


class Car:
    """the final product built through the facade"""
    def __init__(self, model: str, engine: str, transmission: str, color: str):
        self.model = model
        self.engine = engine
        self.transmission = transmission
        self.color = color


class CarBuilder:
    """the complex subsystem: each step has to be called separately and in order"""
    def __init__(self):
        self.model = None
        self.engine = None
        self.transmission = None
        self.color = None

    def build_model(self, model: str) -> None:
        print(f"  [builder] selecting chassis for model {model}")
        self.model = model

    def add_engine(self, engine: str) -> None:
        print(f"  [builder] mounting engine {engine}")
        self.engine = engine

    def add_transmission(self, transmission: str) -> None:
        print(f"  [builder] fitting transmission {transmission}")
        self.transmission = transmission

    def add_color(self, color: str) -> None:
        print(f"  [builder] painting it {color}")
        self.color = color

    def assemble(self) -> Car:
        """put the stored parts together into a Car"""
        return Car(self.model, self.engine, self.transmission, self.color)


class CarFacade:
    """the facade: exposes a single method that runs every builder step"""
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def build_car(self, model: str, engine: str, transmission: str, color: str) -> Car:
        """runs all the building steps in order and returns the finished car"""
        self.builder.build_model(model)
        self.builder.add_engine(engine)
        self.builder.add_transmission(transmission)
        self.builder.add_color(color)
        return self.builder.assemble()


if __name__ == '__main__':
    car_builder = CarBuilder()
    car_facade = CarFacade(car_builder)

    print("Building a car through the facade:")
    car = car_facade.build_car('Sedan', 'Inline 4', '6-speed manual', 'Blue')

    print(car.color, car.model, car.engine, car.transmission)
