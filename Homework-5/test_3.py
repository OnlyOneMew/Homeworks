n = int(input("Enter a natural number:"))

if not 0 < n < 50:
    print("The number is in the range between 0 and 50")
else:
    for i in range(n):
        indent = " " * (n - (i + 1))
        index = i * 2 + 1
        if i == 0:
            print(" " * (n - 2), "*")
            continue

        num_of_slashes = int((index - 1) / 2)
        result = indent + f"{'/' * num_of_slashes}{'|'}" + ('\\' * num_of_slashes)
        print(result)

    print(" " * (n - 2), "|")
