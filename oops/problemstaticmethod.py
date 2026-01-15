class Library_Membership_System:
    def __init__(self,name,age,membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type

    @staticmethod
    def is_valid_age(age):
        return 12 <= age <= 100

    @staticmethod
    def is_valid_membership_type(membership_type):
        return membership_type in ("standard", "premium")
    
    def display_info(self):
        print(f"{self.name} whose {self.age} and {self.membership_type} has a valid library card")

user1 = Library_Membership_System("Amrit",21,"premium")    
if user1.is_valid_age(user1.age) and user1.is_valid_membership_type(user1.membership_type):
    user1.display_info()
else:
    print("not a valid member")    