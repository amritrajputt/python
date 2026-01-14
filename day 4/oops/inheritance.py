# create an electric car class that inherits from the class and has an additional attribute battery_size
class Car:
    def __init__(self,brand,model): #__init__ is constructor
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"     #"F{}" is known as formatted string

class Electric_Car(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        

my_tesla = Electric_Car("tesla","model s","85KWH")
res = my_tesla.model
result =  my_tesla.full_name()
print(result)
print(res)