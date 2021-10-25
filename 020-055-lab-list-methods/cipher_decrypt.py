cipher = input('Enter your encrypted message: ')


def decrypt(cipher):
    result = ""
    # Iterate through the cipher

        # Check whether character is alphanumeric

            # Check whether character is A or a, replace with Z or z




            # Else shift letter one below
            else:

        # Else append character as it is
        else:
            result += char

    return result


print("Cipher was :", cipher)
print("Decrypted message is :", decrypt(cipher))
