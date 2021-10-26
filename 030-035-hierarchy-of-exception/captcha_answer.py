def captcha():
    inp = int(input("3 + 16? "))
    try:
        assert inp == 19

    except AssertionError:
        print("Please try again.")
        captcha()

    print("Correct!")


captcha()
