def captcha():
    inp = int(input("3 + 16? "))
    try:
        assert inp == 19

    except AssertionError:
        print("Wrong input, please try again.")
        captcha()

    except Exception:
        print("Hmm, something went wrong, please try again.")
        captcha()

    print("Correct!")


captcha()
