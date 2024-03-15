n = int(input("Enter number (0 - 9999): "))

while not (0 <= n < 10000):
    n = int(input("Please Enter number (0 - 9999): "))


original_num = n
reversed_num = 0

while n > 0:
    remainder = n % 10
    reversed_num = (reversed_num * 10) + remainder
    n = n // 10

n = original_num
sum_nums = 0
while n > 0:
    sum_nums += n % 10
    n = n // 10

print(f"Entered number is: {original_num}")
print(f"Reversed number is: {reversed_num}")
print(f"Sum of digits: {sum_nums}")
