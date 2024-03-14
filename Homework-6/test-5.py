n = int(input("Enter number up to 10: "))

while n >= 10:
    n = int(input("Please enter number between 1 and 9: "))

space = " "
if 0 < n < 10:
    i = 0
    while i <= n:
        print((space * (n - i)), end="")
        j = i

        while j >= 0:
            print(j, end="")
            j -= 1
        k = 1

        while k <= i:
            print(k, end="")
            k += 1
        print()
        i += 1
else:
    print("Invalid input")
