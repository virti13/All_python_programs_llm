# Parent class
class Vehicle:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Vehicle:", self.name)


# Child class
class Bus(Vehicle):

    def __init__(self, name, fare):
        super().__init__(name)
        self.fare = fare

    def show_info(self):
        super().show()
        print("Bus Fare:", self.fare)


# Create object
bus = Bus("City Bus", 20)

bus.show_info()