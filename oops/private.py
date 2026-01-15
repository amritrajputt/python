class User:
    def __init__(self,email,password):
        self.__email = email # here we prefix email with '__' so that it cannot be changed now we cannot change email outside of class.
        self.password = password
  

user1 = User("aMRit123","12345678")
print(user1.__email)    #cannot be accessed

user1.__email = "amritrajput@1111" #cannot be modified

print(user1.__email) 


# When a variable name starts with double underscore (__) inside a class, Python applies name mangling.
# Python changes the variable name by prefixing it with the class name.
# Because of this, the variable cannot be accessed or modified using its original name from outside the class.
# However, if the mangled name (_ClassName__variable) is used, the variable can still be accessed and modified.
# This mechanism is meant to prevent accidental access, not to enforce true privacy.


class User:
    def __init__(self,email,password):
        self.__email = email 
        # here we prefix email with '__' so that it cannot be changed now we cannot change email outside of class.
        # but after twinking can can chnage and access 
        self.password = password
  

user1 = User("aMRit123","12345678")
print(user1._User__email)    #before modifing

user1._User__email = "amritrajput@1111"

print(user1._User__email) #after modifing


# conclusion :this way it can be modified and accessed and "_User__email" is done by python internally
