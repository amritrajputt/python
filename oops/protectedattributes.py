class User:
    def __init__(self,email,password):
        self._email = email # here we prefix email with '_' so that it cannot be changed but it can be changed but we shouldn't chnaged.
        self.password = password
  

user1 = User("aMRit123","12345678")
print(user1._email)    #before modifing

user1._email = "amritrajput@1111"

print(user1._email) #after modifing


# conclusion : can be accessed and modify both even if it is protected but we should not do this.  
