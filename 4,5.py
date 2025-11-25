plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha():
        char_code = ord(char)

        if char.isupper():
            # przesunięcie z zawijaniem od Z → A
            char_code = ord('A') + (char_code - ord('A') + 1) % 26
        else:
            # przesunięcie z zawijaniem od z → a
            char_code = ord('a') + (char_code - ord('a') + 1) % 26

        char = chr(char_code)

    # spacja i inne znaki bez zmian
    encrypted_text += char

print(plain_text)
print(encrypted_text)
