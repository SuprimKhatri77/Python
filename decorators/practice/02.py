def add_exclamation(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return f"{result}!"
    return wrapper

@add_exclamation
def str_rtn(str):
    return str
print(str_rtn("slash"))