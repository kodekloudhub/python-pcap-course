import math


def circle_area(r):
    return math.pi * r * r


inp = float(input("Enter the radius of a circle:"))
print("Area of circle =", circle_area(inp))
