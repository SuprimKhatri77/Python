def repeat_twice(func):
    def wrapper(*args,**kwargs):
        greet_msg = func(*args,**kwargs)
        print(greet_msg)
        return greet_msg
    return wrapper

@repeat_twice
def greeting(greet):
    return greet
print(greeting("hello"))