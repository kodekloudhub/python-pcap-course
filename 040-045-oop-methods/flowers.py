class Flower:
    def __init__(self, petals=False, thorns=False, color=False):
        self.petals = petals
        self.thorns = thorns
        self.color = color

    def has_color(self, color):
        if self.color:
            return "it has color " + color

    def has_thorns(self, thorns):
        if self.thorns:
            return "it has thorns"

    def season(self, blooming):
        return "it blooms in " + blooming


class Rose(Flower):
    def __init__(self, color):
        # Call the superclass init


    def season(self):
        # return the superclass season and pass as parameter 'spring'



rose = Rose("Red")

# print the rose season


# print the rose superclasses
