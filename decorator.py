""" 
In this file I am exploaring how the Decorators works in python programming 
What is the Decorators

Decorator is special function that wraps another function to add extra behavior with altering original function code
A Decorator 
-> Takes a function as input
-> Adds extra Behavior
-> Returns a new function 
Decorators defined in python like @decorator_name
"""  

# import sys

# def my_decorator(func):
#     def wrapper():
#         print('Before greeting...')
#         func()
#         print('After greeting...') 
#     return wrapper

# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for _ in range(n):
#                 func()
#         return wrapper
#     return decorator

# def logger(func):
#     def wrapper(*args , **kwargs):
#         print('calling: ', func.__name__)
#         result = func(*args , **kwargs)
#         print(f"Result {result}")
#         return result
#     return wrapper
# @my_decorator
# def greeting():
#     print('hello world')
# greeting()

 
# @repeat(4)
# def hello():
#     print('hello world')

# hello()



# @logger
# def add(x, y):
#     return x + y  

# a , b = (int(x) for x in sys.argv[1:])
# add(a, b)

# def give_element(lst:list):
#     def decorator(func):
#         def wrapper():
#             print(func.__name__)
#             for ele in lst:
#                 result = func(*ele )
#                 print(result)
#             return result
#         return wrapper
#     return  decorator
            
        
# @give_element([[1, 2], [3, 4]])
# def add_func(a , b):
#     return a+ b

# add_func()

import time

def timer(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time() 
        print(f"Time Taken : {start - end:.5f}s")
        return result
    return wrapper

@timer
def compute():
    return sum(i * i for i in range(1000000))
compute()






