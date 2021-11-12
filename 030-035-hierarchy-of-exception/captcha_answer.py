def captcha(inp):
    try:
        assert inp == 19
        print("Correct!")
    except AssertionError:
        print("Wrong input, please try again.")


if __name__ == "__main__":
    try:
        inp = int(input("3 + 16? "))
        captcha(inp)
    except Exception:
        print("Hmm, something went wrong, please try again.")
        captcha(inp)
