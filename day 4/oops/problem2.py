# write a method to the car class that displays the full name of the car (brand and car)
class Car:
    def __init__(self,brand,model):
        #__init__ is constructor
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}" 
    #"F{}" is known as formatted string
my_car = Car("toyota","fortuner")    
print(my_car.brand,my_car.model)
print(my_car.full_name())
my_car = Car("maruti","alto 800")
print(my_car.brand,my_car.model)