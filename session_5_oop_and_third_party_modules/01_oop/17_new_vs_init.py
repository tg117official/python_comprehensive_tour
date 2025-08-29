class MyClass:
    def __init__(self):
        print("__init__ method is called")
        self.attribute = "Initialized"

    def __new__(cls):
        print("__new__ method is called")
        instance = super().__new__(cls)  # Memory allocation
        return instance


# Creating an instance of MyClass
obj = MyClass()
print(obj)
print("Object created successfully")

# The MyClass class defines both the __new__ and __init__ methods.

# In the __new__ method, we print a message to indicate that it's being called, and then
# we create and return an instance of the class using super().__new__(cls).

# In the __init__ method, we print a similar message and initialize an attribute.
# Finally, we create an instance of MyClass called obj.


# Creation of the instance:
#       When you create an object of a class, Python automatically calls the __new__ method of
#       that class. This method is responsible for creating the instance of the class. It receives
#       the class itself (cls) as its first argument.
#
# Memory allocation:
#       Inside the __new__ method, memory is allocated for the new object. This is typically done
#       using the super().__new__(cls) call, which invokes the __new__ method of the superclass
#       (usually object class) to create the instance.
#
# Initialization:
#       After the instance is created, it is returned to the caller. At this point, no
#       initialization of the object's attributes has occurred yet. That's where the __init__
#       method comes into play
