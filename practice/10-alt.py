def remove_duplicate(numbers):
    unique_numbers = []

    for i in numbers:
        if i not in unique_numbers:
            unique_numbers.append(i)
    return unique_numbers
numbers = [1,2,3,4,5,6,7,8,7,8,9,1]
print(remove_duplicate(numbers))