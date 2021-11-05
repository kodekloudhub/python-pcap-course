class Desert:
    def __init__(self, flavor):
        self.flavor = flavor


class IceCream(Desert):
    def __init__(self, flavor):
        super().__init__(flavor)

    def __str__(self):
        return "My favorite flavor is " + self.flavor


obj = IceCream("pistachio")
print(obj)
