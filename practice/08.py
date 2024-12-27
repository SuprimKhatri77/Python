def palindrome_check(str):
    char = ""
    for i in str:
        char = i + char
    if char == str:
        print("palindrome")
    else:
        print("not palindrome")
palindrome_check("civic")