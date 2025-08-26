import math

def area_of_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def perimeter_of_rectangle(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative")
    return 2 * (length + width)
