user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

def greeting(name,age):
    print(f"Hey {user_name}! Welcome. You're {user_age}y/o.")

greeting(user_name,user_age)