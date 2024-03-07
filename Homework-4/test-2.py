import random

input_num = input("Enter a positive integer up to 30: ")
if input_num.isdigit():
    n = int(input_num)
    if 0 < n < 30:
        max_value = 0
        for _ in range(n):
            random_int = random.randint(0, 1000)
            print(random_int, end=" || ")
            if random_int > max_value:
                max_value = random_int
        print(f"\nThe maximum value is: {max_value}")
    else:
        print("Please enter a number up to 30")
else:
    print("Please enter only positive integer")
