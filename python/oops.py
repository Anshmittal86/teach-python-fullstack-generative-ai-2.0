# 1. Basic Class and Object:- create a car class with attributes like brand and model. Then create an instance of this class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
my_car = Car("Lamborghini", "Aventador", "Ultra")
print(my_car.brand)
print(my_car.model)


# 2. Class Method and Self: Add a method to the Car Class that displays the full name of the car (brand and model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        print(f"{self.brand} {self.model}")

my_car = Car("Toyota", "Camry")

print(my_car.brand)
print(my_car.model)

print(my_car.full_name())