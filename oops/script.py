class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("whoof whoof")   

class Owner:
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.contact = contact_number

owner1 = Owner("amrit","lucknow",8271425886)
dog1 = Dog("kalua","street",owner1)

dog1.bark()
print(dog1.owner.name)
