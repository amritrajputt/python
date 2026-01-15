class User:
    user_count = 0
    def __init__(self,username,email):
        self.username = username
        self.email = email
        User.user_count+=1
    def display_user(self):
        print(f"Username: {self.username},Email:{self.email}")   


user1 = User("amrit","amrit123") 
print(user1.user_count)
user2 = User("riya","amrit000")
print(user2.user_count)
print(User.user_count)


# static attribute (Sometimes called a class attribute) is an attribute that belongs to the class itself,
# not to any specific instance of the class

#class level attribute attribute is defined on class but can be accessed by class object also

# it is used when any attribute is common to all instance