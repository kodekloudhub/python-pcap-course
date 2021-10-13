import math


def is_triangle(a, b, c):
    if math.hypot(a, b) == c:
        return True
    return False


print("The program checks if three sides form a right-angled triangle.")
inp1 = int(input("Enter first side value: "))
inp2 = int(input("Enter second side value: "))
inp3 = int(input("Enter third side value: "))
print("Is triangle?", is_triangle(inp1, inp2, inp3))
