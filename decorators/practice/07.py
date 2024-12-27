def check_positive(func):
    def wrapper(*args):
        number = func(*args)
        for num in number:
            if num < 0:
                print(f"Negative number found i.e {num}")
                break
            else:
                print(num)
        return number
    return wrapper

@check_positive
def InputNumber(n = [1,2,3,4,-5,7]):
    return n
InputNumber()