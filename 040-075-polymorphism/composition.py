class Train:
    def get_fuels(self):
        return 'diesel'

    def get_speed(self):
        return "200Km/hr"

    def get_type(self):
        return "A train"


class Bus:
    def get_fuels(self):
        return 'electricity'

    def get_speed(self):
        return "80Km/hr"

    def get_type(self):
        return "A bus"


class Transport:
    # Add the constructor with a transport argument

    def travel(self):
        # Get fuels from transport object
        fuels = # complete the code
        # complete code below so outcome is:
        # A bus uses diesel / or A train uses electricity
        return # complete code 

    def distance_covered(self, hrs):
        # Get speed from the transport object
        # use a string method to delete 'Km/hr' part from speed
        # and return an integer
        km = # complete the code
        return (
            # complete code so outcome is:
            # A train covers <km> in <hrs> hours.
            # or A bus covers <km> in <hrs> hours.

        )


train = Transport(Train())
bus = Transport(Bus())

print(train.travel())
print(bus.travel())
print(train.distance_covered(3))
print(bus.distance_covered(3))
