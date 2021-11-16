from os import strerror


def lipogram(letter):
    letter.lower()
    try:
        txt = open("/root/code/oulipo.txt", "r")
    except IOError as e:
        print("I/O error: ", strerror(e.errno))
        txt = None
    except Exception as e:
        print(e)
    else:
        count = sum(map(lambda x: 1 if letter in x else 0, txt))
        print(letter, "appears", count, "times")
    finally:
        if txt:
            txt.close()


lipogram("E")
