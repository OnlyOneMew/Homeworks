def string_reverse(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + string_reverse(string[:-1])


def main():
    words = ["a", "Abc", "Test", "Python", "Bo", "academy", "homework"]
    for word in words:
        print(f"Original string: {word}")
        reversed_string = string_reverse(word)
        print(f"Reversed string: {reversed_string}")


if __name__ == "__main__":
    main()
