# def my_decorator(func):
#     def wrapper():
#         print("Before funs runs")
#         func()
#         print("After funs runs")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello")
# greet()
#----------------------------------------------

# from functools import wraps
# def log_activity(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Finished: {func.__name__}")
#         return result
#     return wrapper

# @log_activity
# def brew(type):
#     print(f"Brewing {type}")

# brew("Pizza")
#------------------------------------------------

# from contextlib import contextmanager
# @contextmanager
# def my_manager():
#     print("Starting")
#     try:
#         yield
#     finally:
#         print("Closing")

# with my_manager():
#     print("Working")
#--------------------------------------------------

# #type hints
# def add(a: int, b: int) -> int:
#     return a + b

# print(add(10, 20))
#----------------------------------------------------

# def greet(name: str | None) -> str:
#     if name is None:
#         return "Hello Guest"
#     return "Hello " + name

# print(greet("Aman"))
# print(greet(None))
#----------------------------------------------------

from functools import wraps

# def log_activity(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Finished: {func.__name__}")
#         return result
#     return wrapper

# @log_activity
# def brew_chai(type):
#     print(f"Brewing {type} chai")

# brew_chai("Masala")
#--------------------------------------------------

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: admins only")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_tea_inventory(role):
    print("Access granted to tea inventory")

access_tea_inventory("user")
access_tea_inventory("admin")
#-----------------------------------------