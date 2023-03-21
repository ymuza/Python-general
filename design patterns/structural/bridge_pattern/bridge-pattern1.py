"""This pattern decouples the abstraction from the implementation"""


class VehicleDrawing:
    def __init__(self, color):
        self._color = color

    def draw(self):
        pass


class Car(VehicleDrawing):
    def draw(self):
        return f"Drawing a {self._color} car"


class Truck(VehicleDrawing):
    def draw(self):
        return f"Drawing a {self._color} truck"


class RedVehicle(VehicleDrawing):
    def __init__(self, vehicle_drawing):
        super().__init__('red')
        self._vehicle_drawing = vehicle_drawing

    def draw(self):
        return self._vehicle_drawing.draw()


car = Car('blue')
red_car = RedVehicle(car)
print(red_car.draw())

truck = Truck('green')
red_truck = RedVehicle(truck)
print(red_truck.draw())
