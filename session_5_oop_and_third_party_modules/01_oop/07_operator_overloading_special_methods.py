class Vector:
    def __init__(self, x, y):
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate

    # Overloading the addition operator
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
        # self : refers to the instance of the class (Vector in this case) on which the __add__ method is called.
        # other : is the instance of Vector that is passed to the method to be added to self.

        # 1. Method Definition (`__add__`):
        #    - `__add__(self, other)` is a special method in Python known as a "dunder"
        #    (double underscore) method. It allows you to define the behavior of the addition operator
        #    `+` when used on instances of your class. When you write `v1 + v2`, Python automatically
        #    calls `v1.__add__(v2)`.
        #
        # 2. Type Checking (`isinstance`):
        #    - `if isinstance(other, Vector):` checks if the `other` object passed to the method is
        #    an instance of the `Vector` class. This is important because you only want to define
        #    addition for two vectors. Type checking ensures that your method handles only appropriate
        #    input, thereby avoiding errors that would occur if `other` were not a `Vector`
        #    (like a number or a string).
        #
        # 3. Performing the Addition:
        #    - `return Vector(self.x + other.x, self.y + other.y)`
        #    - If `other` is indeed a `Vector`, it performs element-wise addition of the vectors:
        #      - `self.x + other.x` adds the x-components of the two vectors.
        #      - `self.y + other.y` adds the y-components of the two vectors.
        #    - A new `Vector` instance is then created with these summed components and returned. This
        #    is the result of the addition operation.
        #
        # 4. Handling Unsupported Types (`NotImplemented`):
        #    - `return NotImplemented`
        #    - If `other` is not an instance of `Vector`, the method returns `NotImplemented`. This is
        #    a special value used in Python to indicate that the operation is not implemented for the
        #    given type combination. Returning `NotImplemented` allows Python's interpreter to handle it
        #    appropriately. It may lead to:

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
res = (v1.x + v2.x)
result = v1 + v2 # v1.__add__(v2)
print(result)  # Outputs: Vector(7, 10)

# Subtract two vectors
result = v1 - v2
print(result)  # Outputs: Vector(-3, -4)
