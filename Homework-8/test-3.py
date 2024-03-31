word = input("Enter a word: ")

length = len(word)

if length % 2 == 0:
    middle = length // 2 - 1, length // 2
    is_even = True
else:
    middle = length // 2
    is_even = False

count = 0
while count < 1:
    print(word[-1] * 5)
    print(word[0] * 5)

    if is_even:
        print((word[middle[0]] + word[middle[1]]) * 5)
    else:
        print(word[middle] * 5)

    count += 1
