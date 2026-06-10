from functools import wraps
def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling Function: '{func.__name__}' with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished calling'{func.__name__}' with result: {result}")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    return a + b
print(add(5,b=10))