class Position:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Layout:
    def __init__(self, start, coord_x, coord_y):
        self.position1 = start
        self.position2 = coord_x
        self.position3 = coord_y

    def textbox(self):
        length = self.position2.get_x() - self.position1.get_x()
        breadth = self.position3.get_y() - self.position1.get_y()

        area = length * breadth
        return area


layout = Layout(Position(0, 0), Position(3, 0), Position(0, 5))
print(layout.textbox())
