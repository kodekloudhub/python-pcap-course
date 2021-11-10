from os import strerror


def lipogram(letter):
    letter.lower()
    # Write a try/except block to open the file
    # and handle an IOError
    try:

    except IOError as e:
        # print the error with the use of strerror and errno
        txt = None
    except Exception as e:
        print(e)
    else:
        # Do the count here using sum(), map(), lambda
        # to count occurences of the letter
        print(letter, "appears", count, "times")
    finally:
        if txt:
            txt.close()


lipogram("E")
