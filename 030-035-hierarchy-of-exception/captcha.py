def captcha():
    inp = int(input("3 + 16? "))
    try:
        if inp == 19:
            print("Correct!")
        else:
            print("Wrong input, please try again.")
    except Exception:
        print("Hmm, something went wrong, please try again.")
        captcha()


captcha()
