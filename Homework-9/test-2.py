text_input = input("Enter string: ")
second_input = input("Enter string: ")

print(text_input)
print(second_input)

possible = True

for char in second_input:
    if char not in text_input:
        possible = False
        break
    text_input = text_input.replace(char, '', 1)
if possible:
    print("YES")
else:
    print("NO")
