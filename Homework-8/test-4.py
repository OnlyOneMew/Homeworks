row_1 = "qwertyuiop"
row_2 = "asdfghjkl"
row_3 = "zxcvbnm"

action = input("Enter 'e' for encryption, 'd' for decryption: ")

if action.lower() == 'e':
    text = input("Enter text: ")
    encrypted_text = ''
    for char in text:
        if char.lower() in row_1 + row_2 + row_3:
            if char in row_1:
                encrypted_text += row_1[(row_1.index(char) + 1) % len(row_1)]
            elif char in row_2:
                encrypted_text += row_2[(row_2.index(char) + 1) % len(row_2)]
            elif char in row_3:
                encrypted_text += row_3[(row_3.index(char) + 1) % len(row_3)]
        else:
            encrypted_text += char
    print("Encrypted:", encrypted_text)

elif action.lower() == 'd':
    text = input("Enter text: ")
    decrypted_text = ''
    for char in text:
        if char.lower() in row_1 + row_2 + row_3:
            if char in row_1:
                decrypted_text += row_1[(row_1.index(char) - 1) % len(row_1)]
            elif char in row_2:
                decrypted_text += row_2[(row_2.index(char) - 1) % len(row_2)]
            elif char in row_3:
                decrypted_text += row_3[(row_3.index(char) - 1) % len(row_3)]
        else:
            decrypted_text += char
    print("Decrypted:", decrypted_text)

else:
    print("Please enter e or d.")
