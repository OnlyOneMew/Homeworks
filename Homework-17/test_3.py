str_1 = ["iphone", "bottle", "converse", "saw", "lamp"]
str_2 = ["samsung", "bee", "orange", "apple", "sofa"]
str_3 = ["computer", "monitor" "mouse", "key", "keyboard"]

print(str_1)
print(str_2)
print(str_3)

merged_list = str_1 + str_2 + str_3
filtered_words = filter(lambda x: len(x) <= 3, merged_list)


for word in filtered_words:
    print(word.upper())
