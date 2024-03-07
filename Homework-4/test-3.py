input_num = input("Enter a positive number: ")
if input_num.isdigit():
    n = int(input_num)
    if 0 < n < 1000:
        print(f"Divisors of {n}: ", end=" ")
        for divisor in range(1, n + 1):
            if n % divisor == 0:
                print(divisor, end=" | ")
    elif n == 0:
        print("The number has no divisor")
    else:
        print("Please enter a positive number up to 1000")
else:
    print("Please enter positive integer")
