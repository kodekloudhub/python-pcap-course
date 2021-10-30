def captcha():
    try:
        inp = int(input("3 + 16? "))
        assert inp == 19
        print("Correct!")

    except AssertionError:
        print("Wrong input, please try again.")
        captcha()

    except Exception:
        print("Hmm, something went wrong, please try again.")
        captcha()


captcha()
