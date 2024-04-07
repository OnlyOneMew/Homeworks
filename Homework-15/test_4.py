def vowels_counter(string):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


def main():
    words = ["Abc", "Test", "Python", "Bookmark", "academy", "homework"]
    for word in words:
        count_vowels = vowels_counter(word)
        print(f"There are {count_vowels} vowel in {word}")


if __name__ == "__main__":
    main()
