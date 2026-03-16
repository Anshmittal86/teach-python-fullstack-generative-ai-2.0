import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {start - end} seconds to execute.")
        return result
    return wrapper
    
@timer
def slow_function():
    time.sleep(2)
    print("Done")
    
slow_function()

