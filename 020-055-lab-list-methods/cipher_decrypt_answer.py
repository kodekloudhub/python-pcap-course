cipher = input('Enter your encrypted message: ')


def decrypt(cipher):
    result = ""
    # Iterate through the cipher
    for char in cipher:

        # Check whether character is alphanumeric
        if char.isalpha():
            if char == 'A':
                result += 'Z'
            elif char == 'a':
                result += 'z'
            else:
                result += chr(ord(char) - 1)
        else:
            result += char

    return result


print("Cipher was :", cipher)
print("Decrypted message is :", decrypt(cipher))
