from functools import wraps
def auth_decorator(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role == "admin":
            print("Authentication successful!")
        else:
            print("Access denied.")
    return wrapper



@auth_decorator
def access_sensitive_data(user_role):
    print("Accessing sensitive data...")

access_sensitive_data("admin")