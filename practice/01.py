def numbers(a,b):
    print(f"Before Swapping a ={a}, b = {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After Swapping a ={a}, b = {b}")

numbers(1,7)