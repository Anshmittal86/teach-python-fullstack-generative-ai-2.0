import functools

# Task 1: Function Execution Logger
def logger_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished function: {func.__name__}")
        return result
    return wrapper
    
@logger_function
def say_hello():
    print("Hello")

@logger_function
def squareOf(number):
    print(number ** 2)

say_hello()
squareOf(5)