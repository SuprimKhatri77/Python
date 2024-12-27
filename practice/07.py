def reverse_str(str):
    char = ""
    for i in str:
     char = i + char
    print(f"Given string: {str}, Reversed string: {char}")
reverse_str("abcd")