def division():
    global number1, number2
    number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")
    try:
        print(float(number1) / float(number2))
    except ZeroDivisionError:
        print("Zero division error, please try again.")
        division()
    except TypeError:
        print("Please enter valid numbers.")
        division()
    except Exception:
        print("Hmm, something went wrong, try again.")
        division()


division()
