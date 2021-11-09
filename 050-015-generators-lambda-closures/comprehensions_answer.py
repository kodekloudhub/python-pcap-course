mix_list = [1, "Python", 0.5, "Apple", 3.0, "\n"]
numbers = list(filter(
    lambda n: isinstance(n, float) or isinstance(n, int), mix_list
    ))

print(numbers)
