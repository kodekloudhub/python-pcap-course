from random import random, seed


def random_seed(s):
    seed(s)
    return random()


s = float(input("Enter a value: "))
print(random_seed(s))
