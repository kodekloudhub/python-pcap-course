class A:
    var = 1

    def __init__(self, value=2):
        self.value = value


a = A()

# Use var or value inside the hasattr()
print(hasattr(a, ...) is True)
print(hasattr(A, ...) is True)
print(hasattr(A, ...) is False)
print(hasattr(a, ...) is True)
