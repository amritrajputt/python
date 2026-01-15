# static method in python is a method that belongs to the class itself 
# rather than any instance of the class

# to define a static method , we use the '@staticmethod' decorator


class BankAccount:
    MIN_BALANCE = 1000
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance

    def deposite(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s balance is {self._balance}")  
        else:
            print("deposite amount must be positive")

    @staticmethod
    def is_valid_intrest_rate(rate):
        return 0<=rate<=5

account = BankAccount("Amrit",10)
account.deposite(2000)           
print(BankAccount.is_valid_intrest_rate(5)) 
