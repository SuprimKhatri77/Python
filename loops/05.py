input_str = input("Provide me a string:")

for char in input_str:
    if input_str.count(char) == 1:
        print('Non repeated char is: ',char)
        break
    