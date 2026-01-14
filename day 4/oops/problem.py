class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        #__init__ is constructor
my_car = Car("toyota","fortuner")    
print(my_car.brand,my_car.model)
my_car = Car("maruti","alto 800")
print(my_car.brand,my_car.model)