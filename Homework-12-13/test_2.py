from test_1 import modify_str


def word_is_match(str_1, str_2):
    for _ in range(len(str_1)):
        str_1 = modify_str(str_1)
        if str_1 == str_2:
            return True
    return False


def main():
    str_1 = input("Enter a string: ").strip()
    str_2 = input("Enter a string: ").strip()
    if word_is_match(str_1, str_2):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
