from test_2 import generate_random_nums


def remove_duplicate_numbers(numbers):
    unique_numbers = list(set(numbers))
    return unique_numbers


def main():
    numbers = generate_random_nums()
    unique_numbers = remove_duplicate_numbers(numbers)
    print("List:", unique_numbers)
    print("Length:", len(unique_numbers))


if __name__ == '__main__':
    main()
