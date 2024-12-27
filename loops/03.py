num = 7
res = 0
for i in range(1,num+4):
    res = i * num
    if i == 5:
        continue
    print(f'{num} x {i} = {res}')  