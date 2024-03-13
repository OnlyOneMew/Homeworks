DB_PASSWORD = "Georgia"
MAX_TRIES = 3

for _ in range(MAX_TRIES):
    input_password = input("Please enter password: ")
    if input_password == DB_PASSWORD:
        print("Hello from Georgia")
        break
    else:
        print("Incorrect password, Try again")
else:
    print("You are blocked!!!")
