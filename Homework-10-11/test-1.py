n = int(input("Enter number greater than 1: "))
if n <= 1:
    print("Please enter number greater then 1: ")
    exit(1)

x = 0
alternate_sign = 1
for i in range(1, n + 1):
    x += alternate_sign * 1 / (2 * i - 1)
    alternate_sign *= -1
x *= 4
print(x)

# n ის გაზრდით  PI მნიშვნელობასთან უფრო და უფრო ახლოს მივდივარ