"""This pattern allows us to create a simplified interface to a complex system of classes,
making it easier to use and reducing the overall complexity of the code."""


class Car:
    def __init__(self, model: str, engine: str, transmission: str, color: str):
        self.model = model
        self.engine = engine
        self.transmission = transmission
        self.color = color


class CarBuilder:
    def build_model(self, model: str) -> None:
        # Code to select the car model
        pass

    def add_engine(self, engine: str) -> None:
        # Code to add the engine to the car
        pass

    def add_transmission(self, transmission: str) -> None:
        # Code to add the transmission to the car
        pass

    def add_color(self, color: str) -> None:
        # Code to add the color to the car
        pass


class CarFacade:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def build_car(self, model: str, engine: str, transmission: str, color: str) -> Car:
        self.builder.build_model(model)
        self.builder.add_engine(engine)
        self.builder.add_transmission(transmission)
        self.builder.add_color(color)
        return Car(model, engine, transmission, color)


if __name__ == '__main__':
    car_builder = CarBuilder()
    car_facade = CarFacade(car_builder)

    car = car_facade.build_car('Sedan', 'Inline 4', '6-speed manual', 'Blue')

    print(car.color, car.model, car.engine)
