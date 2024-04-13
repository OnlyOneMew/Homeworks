import random

random_numbers = [random.randint(10,1000000000) for _ in range(100)]
shortest_num = min(random_numbers, key = lambda x: len(str(x)))
longest_num = max(random_numbers, key= lambda x: len(str(x)))

ascending_order = sorted(random_numbers, key= lambda x: len(str(x)))

descending_order = sorted(random_numbers, key= lambda x: len(str(x)))

print("Random numbers: ", random_numbers)
print("Shortest number: ", shortest_num)
print("Longest number: ", longest_num)
print("Numbers sorted by length in ascending order:", ascending_order)
print("Numbers sorted by length in descending order:", descending_order)