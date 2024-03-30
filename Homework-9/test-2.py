text_input = input("Enter string: ")
second_input = input("Enter string: ")

print(text_input)
print(second_input)

possible = True

if len(text_input) != len(second_input):
    possible = False

for char in second_input:
    if char not in text_input:
        possible = False
        break

if possible:
    print("YES")
else:
    print("NO")
