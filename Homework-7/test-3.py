n = int(input("Enter number (0 - 9999): "))

while not (0 <= n < 10000):
    n = int(input("Please Enter number (0 - 9999): "))


original_num = n
reversed_num = 0
sum_nums = 0

while n > 0:
    remainder = n % 10
    reversed_num = (reversed_num * 10) + remainder
    sum_nums += remainder
    n = n // 10

str_num = str(reversed_num)
zeros = len(str(original_num)) - len(str_num)

if zeros > 0:
    str_num = ("0" * zeros) + str_num

print(f"Entered number is: {original_num}")
print(f"Reversed number is: {str_num}")
print(f"Sum of digits: {sum_nums}")
