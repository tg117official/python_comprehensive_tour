# In Python, the term "object class" refers to the default class from which all other
# classes inherit, called the "object" class. It's the base class for all classes in Python.
#
# Every class you create in Python implicitly inherits from the object class, even if you
# don't explicitly specify it. The object class provides default methods like `__init__`,
# `__str__`, and `__repr__`, which are inherited by all other classes unless overridden.
#
# In simple terms, the object class is like the blueprint for all other classes in Python.
# It defines basic behaviors and properties that all objects in Python share.

# Define a custom class without explicitly inheriting from any other class
class MyClass:
    def __init__(self, x):
        self.x = x
    def say_hello(self):
        print("Hello, Human!!")

# Create an instance of MyClass
obj = MyClass(5)

# Print the type of obj
print("Type of obj:", type(obj))

# Print the type of MyClass
print("Type of MyClass:", type(MyClass))

print(help(MyClass))

# Print whether MyClass is a subclass of the object class
print("Is MyClass a subclass of object class?", issubclass(MyClass, object))
