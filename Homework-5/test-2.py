for i in range(1, 10):
    for j in range(1, i + 1):
        mult_table = i * j
        print(f"{j} * {i} = {mult_table}", end="\t")
    print()
