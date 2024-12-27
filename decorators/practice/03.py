def log_function_call(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        return func.__name__
    return wrapper

@log_function_call
def greet():
    pass
print(greet())