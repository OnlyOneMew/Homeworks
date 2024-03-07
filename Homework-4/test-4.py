input_number = input("Enter a non negative integer up to 20: ")

if input_number.isdigit():
    n = int(input_number)
    if 0 <= n < 20:
        if n == 0:
            num_term = 0
            print(f"The {num_term}th term of the sequence is 0")
        elif n == 1:
            num_term = 1
            print(f"The {num_term}st term of the sequence is 1")
        else:
            term_1, term_2 = 0, 1

            for _ in range(2, n + 1):
                num_term = term_1 + term_2
                term_1, term_2 = term_2, num_term

            print(f"The {n}th term of the sequence is: {num_term}")
    else:
        print("Please enter a integer up to 20")

else:
    print("Input is not valid, enter number up to 20(non-negative)")
