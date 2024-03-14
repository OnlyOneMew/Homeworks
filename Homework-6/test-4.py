n = int(input("Enter a number up to 10: "))

while n <= 0 or n >= 10:
    print("Please enter number between(1-9) ")
    n = int(input("Enter a number up to 10: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1

i = n - 1
while i >= 1:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i -= 1
