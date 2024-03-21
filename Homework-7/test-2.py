n = int(input("Enter number (0 - 1000: "))

while not (0 < n <= 1000):
    n = int(input("Enter number (0 - 1000: "))

print(n, end=" ")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print("->", n, end=" ")
