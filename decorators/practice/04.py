def ToUppercase(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        return res.upper()
    return wrapper

def add_asterisks(func):
    def wrapper(*args,**kwargs):
        return "***" + func(*args,**kwargs) + "***"
    return wrapper

@add_asterisks
@ToUppercase
def name_func(str):
    return str
print(name_func("slashyy"))
