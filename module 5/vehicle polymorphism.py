class Vehicle:

    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):

    def move(self):
        print("Car is driving")


class Bus(Vehicle):

    def move(self):
        print("Bus is running")


# Create objects
car = Car()
bus = Bus()

car.move()
bus.move()