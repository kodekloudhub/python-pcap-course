def captcha():
    inp = int(input("3 + 16? "))
    try:
        if inp == 19:
            print("Correct!")
        else:
            print("Please try again.")
    except Exception:
        print("Please try again.")
        captcha()


captcha()
