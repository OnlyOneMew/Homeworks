input_number = int(input("Enter number from 1 to 10: "))

if 1 < input_number <= 10:
    print(f"Prime divisors of {input_number} : ")
    for i in range(2, input_number + 1):
        if input_number % i == 0:
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print(i, end=' ')
else:
    print("Please enter number from 1 to 10")
