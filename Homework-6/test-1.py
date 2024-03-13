i = 1
while i <= 9:
    j = 1
    while j <= i:
        mult_table = i * j
        print(f"{j} * {i} = {mult_table}", end="\t")
        j += 1
    print()
    i += 1
