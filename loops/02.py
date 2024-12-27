number = int(input('Enter a number: '))
sum = 0

for num in range(number):
    if num % 2 == 0:
        sum += num
print(sum)