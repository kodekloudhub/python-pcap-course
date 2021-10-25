msg = input("Enter your message to encrypt: ")


def encrypt(msg):
    result = ""

    # iterate through the input msg
    for i in range(len(msg)):
        char = msg[i]
        # Check if character is alphanumeric

            # Check char is either Z or z and append A, a respectively




            # Else shift to the next letter


        # If char not alphanumeric just continue

        return result


print("Message to encrypt : ", msg)
print("Cipher: ", encrypt(msg))
