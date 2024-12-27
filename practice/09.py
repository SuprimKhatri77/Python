def comparision ():
    numbers = [1,2,3,88,4,5,6,7,-8]

    max_num = min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
                max_num = num
    return max_num,min_num
print(comparision())
