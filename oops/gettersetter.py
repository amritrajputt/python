class User:
    def __init__(self,email,password):
        self._email = email 
        self.password = password
  
    def get_email(self):  #getter method
        return self._email
    
    def set_email(self,new_email): #setter method
        self._email = new_email
        
    
user1 = User("aMRit123","12345678")

print(user1.get_email())  #got default(1st) email

user1.set_email("amrit123456789")

print(user1.get_email()) #got email after changing (after setter called)

class PropertyDecorator:
    def __init__(self,age):
        self._age = age

# getter : how to get the vlaue
    @property
    def age(self):
        return self._age + 2  

# setter :how we set the value
    @age.setter
    def age (self,age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError ("Tea leaf age must be between 1 and 5 years")    