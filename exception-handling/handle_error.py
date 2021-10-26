def division():
    global number1, number2
    number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")

    if not (number1.isnumeric() and number2.isnumeric()):
        print("Please enter valid numbers.")
        division()
    if float(number2) == 0:
        print("Zero division error, please try again.")
        division()
    elif float(number2) != 0:
        print(float(number1) / float(number2))
    else:
        print("Hmm, something went wrong, try again.")
        division()


division()
