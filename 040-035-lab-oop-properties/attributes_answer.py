class A:
    var = 1

    def __init__(self, value=2):
        self.value = value


a = A()

# Use var or value inside the hasattr()
print(hasattr(a, "var") is True)
print(hasattr(A, "var") is True)
print(hasattr(A, "value") is False)
print(hasattr(a, "value") is True)
