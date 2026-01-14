class Car:
    total_car = 0
    def __init__(self,brand,model): #__init__ is constructor
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand+" !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"     #"F{}" is known as formatted string

    def fuel_type(self):
        return "petrol or diesel"



class Electric_Car(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"

my_tesla = Electric_Car("tesla","model s","85KWH")
print(my_tesla.fuel_type())

safari  = Car("tata","safari")
print(safari.fuel_type())

safarithree = Car("tata","nexon")
print(safari.fuel_type())

print(Car.total_car)