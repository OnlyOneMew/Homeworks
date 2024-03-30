def is_valid_str(input_str):
    return input_str.isalpha()


def modify_str(input_str):
    shifted_str = input_str
    for _ in range(len(input_str)):
        shifted_str = shifted_str[-1] + shifted_str[:-1]
        print(shifted_str)


def main():
    input_str = input("Input string: ").strip()
    if not is_valid_str(input_str):
        print("Please enter only alphabets")
    modify_str(input_str)


if __name__ == "__main__":
    main()
