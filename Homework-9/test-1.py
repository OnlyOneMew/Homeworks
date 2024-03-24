user_input = input("Enter text: ").lower()

str_text = ''.join(char for char in user_input if char.isalpha())
is_palindrome = str_text == str_text[::-1]

if is_palindrome:
    print("Is palindrome")
else:
    print("Is not palindrome")
