class Desert:
    def __init__(self, flavor):
        self.flavor = flavor


class IceCream(Desert):
    def __init__(self, flavor):
        Desert.__init__(self, flavor)

    # Add a custom string representation


# Create an object IceCream with a pistachio flavor

print(obj)
