class User:
    def __init__(self,email,password):
        self._email = email 
        self.password = password
  
    @property
    def email(self):  #getter property
        print('Email accessed')
        return self._email
    
    @email.setter
    def email(self,new_email): #setter property
        self._email = new_email
        
    
user1 = User("aMRit123","12345678")

print(user1.email)  
user1.email="amrit123"
print(user1.email)  