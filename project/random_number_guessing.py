import random

Total_chances = 5

def guess_random_num():
    global Total_chances
    random_number = random.randint(1, 10)  

    for attempt in range(1, 6):  
        if Total_chances > 0:
            try:
                user_guess = int(input(f"Attempt {attempt}: Enter a number between 1-10: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            if user_guess == random_number:
                print(f"You won! Your guess: {user_guess}, Random Number: {random_number}")
                print(f"Chances left: {Total_chances}")
                break
            else:
                Total_chances -= 1
                print(f"You lost! Your guess: {user_guess}, Random Number: {random_number}")
                print(f"Chances left: {Total_chances}")
        else:
            print("Oops! No more chances.")
            break

guess_random_num()
