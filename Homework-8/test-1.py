text_input = input("Enter string: ")

# with for loop

# for char in range(len(text_input)):
#     if char % 2 == 0:
#         if text_input[char] != "e":
#             print(text_input[char], end="")

# with while loop

index = 0
while index < len(text_input):
    if index % 2 == 0:
        if text_input[index] != "e":
            print(text_input[index], end="")

    index += 1
