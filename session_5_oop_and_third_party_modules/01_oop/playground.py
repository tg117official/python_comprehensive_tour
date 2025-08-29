class Vector:
    def __init__(self, x, y):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate

    # Overloading the addition operator
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    # Overloading the subtraction operator
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    # Overloading the string representation method, for easy printing of the object
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage:
v1 = Vector(2, 3)
v2 = Vector(5, 7)

# Add two vectors
# res = (v1.x + v2.x)
result = v1 + v2 # v1.__add__(v2)
print(result)  # Outputs: Vector(7, 10)

# Subtract two vectors
result = v1 - v2
print(result)  # Outputs: Vector(-3, -4)
