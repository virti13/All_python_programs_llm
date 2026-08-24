# Parent class
class Vehicle:
    
    def vehicle_info(self):
        print("This is a vehicle")


# Child class
class Bus(Vehicle):
    
    def bus_info(self):
        print("This is a bus")


# Create object
bus = Bus()

# Call parent class method
bus.vehicle_info()

# Call child class method
bus.bus_info()