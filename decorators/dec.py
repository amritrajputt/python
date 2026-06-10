from functools import wraps
# a decorator is a function that adds extra functionality to another function without modifying its original code.
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("before function runs")
        func()
        print("after function runs")
    return wrapper  

@my_decorator
def greet():
    print("hello from decorators class")    

greet()
print(greet.__name__)  
# Problem: Decorator lagne ke baad function ka original name aur metadata
# lost ho jata hai, sirf 'wrapper' dikhta hai.
# Solution: @wraps original function ki metadata preserve karta hai.   