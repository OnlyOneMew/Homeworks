n = int(input("Enter positive number up to 20: "))

while not (0 <= n < 20):
    n = int(input("Enter positive number (1 - 19):"))

num_1 = 0
num_2 = 1
sum_nums = num_1 + num_2
counter = 0

while counter < n:
    counter += 1
    print(num_1, end=" ")
    sum_nums = num_1 + num_2
    num_1 = num_2
    num_2 = sum_nums
