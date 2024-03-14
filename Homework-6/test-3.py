import random

random_num = random.randint(0, 100)

MAX_ATTEMPT = 10
attempt = 0

while attempt < MAX_ATTEMPT:
    user_input = int(input("Guess the number from 0 to 100: "))
    if user_input < 0 or user_input > 100:
        print("Please enter number up to 100")
        continue
    print(f"Attempt {attempt + 1} / {MAX_ATTEMPT}")
    if user_input == random_num:
        print(f"Random number was {random_num}, You are WINNER !!")
        break
    elif user_input < random_num:
        print("Low, try again")
    else:
        print("High, Try again")

    attempt += 1
    if attempt == MAX_ATTEMPT:
        print()
        print(f"Random Number was: {random_num}")
        print("Computer WINS!")
