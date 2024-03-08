input_num = input("Enter a natural number up to and including 50: ")

if input_num.isdigit():
    number = int(input_num)
    if 0 < number <= 50:
        for num in range(1, number + 1):
            divisors = 0
            print(f"{num} -", end=" ")

            for i in range(1, num + 1):
                if num % i == 0:
                    print(i, end=" ")
                    divisors += 1

                if divisors == 3:
                    break
            print()
    elif number == 0:
        print("Zero cannot be divided")
    else:
        print("Please enter a natural number up to and including 50")
else:
    print("Please enter only number")
