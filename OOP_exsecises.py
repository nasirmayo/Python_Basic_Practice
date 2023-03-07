# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
'''class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 50)
print(modelX.max_speed, modelX.mileage)'''

# OOP Exercise 2: Create a Vehicle class without any variables and methods
class Vehicle:
    pass

# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
'''class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

mmodelX = Bus("School Volvo", 180, 12)
print(mmodelX.name, mmodelX.max_speed, mmodelX.mileage)'''

# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity()
# a default value of 50.

'''class Vehicle:
    def __init__(self, max_speed, mileage, name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name

    def seating_capacity(self, capacity = 50):
        return f"The seating capcity of {self.name} is {capacity} passegers"

class Bus(Vehicle):

    def __init__(self, max_speed, mileage, name, color):
        super().__init__(max_speed, mileage, name)
        self.color = color

    def seating_capacity(self, capacity = 70):
        return super().seating_capacity(capacity=60)

vehicle = Bus(250, 20, "Volvo School", "Yellow")
print(vehicle.seating_capacity(100))'''

# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
'''class Vehicle:
    color = "White"
    def __init__(self, max_speed, mileage, name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
    def display_features(self):
        return f"Color: {self.color}, Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"

class Bus(Vehicle):
    pass
class Bike(Vehicle):
    pass

bus_obj = Bus(250, 20, "Volvo School")
detail = bus_obj.display_features()
print(detail)

bike_obj = Bike(200, 60, "Honda")
bike_obj.color = "Red"
detail = bike_obj.display_features()
print(detail)'''




