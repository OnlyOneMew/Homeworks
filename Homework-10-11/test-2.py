import random
import math

n = int(input("Enter the number greater than 1: "))
if n <= 1:
    print("Please enter number greater than 1 ")
    exit(1)

counter = 0

for i in range(n):
    a = random.random()
    b = random.random()
    if math.sqrt(a ** 2 + b ** 2) <= 1:
        counter += 1
result = 4 * counter / n
print(result)
