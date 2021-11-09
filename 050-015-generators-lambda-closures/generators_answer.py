def counter(n):
    i = 0
    while i <= n:
        yield i
        i += 1


c = counter(3)
print(next(c), next(c), next(c), next(c))
