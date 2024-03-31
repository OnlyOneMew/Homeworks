word = input("Enter a word: ")

vowels = "aeiouAEIOU"
constants = ""

# for loop

# for char in word:
#     if char not in vowels:
#         constants += char
# print(constants)


# while loop

index = 0
while index < len(word):
    if word[index] not in vowels:
        constants += word[index]
    index += 1
print(constants)
