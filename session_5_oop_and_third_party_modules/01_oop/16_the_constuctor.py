# class PersonWithoutInit:
#     def set_info(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_info(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#
# # Create instances of the Person class without __init__
# person1 = PersonWithoutInit()
# person1.set_info("Alice", 30)
#
# person2 = PersonWithoutInit()
# person2.set_info("Bob", 25)
#
# # Display the details of each person using the display_info method
# print("Person 1:")
# person1.display_info()
# print()
#
# print("Person 2:")
# person2.display_info()



class PersonWithInit:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create instances of the Person class with __init__
person1 = PersonWithInit("Alice", 30)
person2 = PersonWithInit("Bob", 25)

# Print out the details of each person
print("Person 1:")
print("Name:", person1.name)
print("Age:", person1.age)
print()

print("Person 2:")
print("Name:", person2.name)
print("Age:", person2.age)


# In object-oriented programming (OOP), a constructor is a special method that is automatically
# called when a new instance (object) of a class is created. The primary purpose of a constructor
# is to initialize the newly created object and prepare it for use.
#
# Constructors are responsible for setting initial values to the attributes of the object,
# performing any necessary setup operations, and ensuring that the object is in a valid state
# upon creation.
#
# In summary, a constructor in OOP serves as the entry point for initializing objects, ensuring
# that they are properly set up and ready for use.



