import math


def calculation(radius):
    area = round(math.pi * radius ** 2,2)
    circumference = round(2 * math.pi * radius,2)
    return area , circumference


print(calculation(7))