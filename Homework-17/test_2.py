import random

list_1 = [random.randint(1, 10) for _ in range(10)]
list_2 = [random.randint(1, 10) for _ in range(10)]
list_3 = [random.randint(1, 10) for _ in range(10)]

print(list_1)
print(list_2)
print(list_3)

sums = list(map(lambda x, y, z: x + y + z, list_1, list_2, list_3))

for i in range(len(list_1)):
    print(f"Sum at index {i}: {sums[i]}")
