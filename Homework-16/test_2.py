import random


def generate_random_nums():
    random_numbers = []
    for _ in range(50):
        random_numbers.append(random.randint(1, 30))
    return random_numbers


def main():
    random_numbers = generate_random_nums()
    expanded_list = []
    for num in random_numbers:
        for _ in range(num):
            expanded_list.append(num)
    print(f"List - {expanded_list}")
    print(f"Length - {len(expanded_list)}")


if __name__ == "__main__":
    main()

