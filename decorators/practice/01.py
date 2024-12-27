def greet_decorator(func):
    def wrapper(*args):
        result = func(*args)
        return result
    return wrapper


@greet_decorator
def greet(name,greeting):
    return F"{greeting} {name}"
print(greet("slash","hello"))