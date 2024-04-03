def modify_str(input_str):
    shifted_str = input_str[-1] + input_str[:-1]
    return shifted_str


def main():
    input_str = input("Input string: ").strip()
    for _ in range(len(input_str)):
        input_str = modify_str(input_str)
        print(input_str)


if __name__ == "__main__":
    main()
