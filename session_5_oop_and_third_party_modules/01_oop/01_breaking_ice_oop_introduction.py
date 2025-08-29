# Define a class named Car
class Car:
    # __init__ is the initializer method that's automatically called when a new object is created.
    def __init__(self, make, model, year):
        # Attributes are variables associated with an object.
        self.make = make  # Make of the car, e.g., "Toyota"
        self.model = model  # Model of the car, e.g., "Corolla"
        self.year = year  # Year of the car, e.g., 2022
        # Additional attribute to track the mileage
        self.mileage = 0

    # A method to describe the car
    def describe(self):
        return f"{self.year} {self.make} {self.model}"

    # A method to update the mileage
    def update_mileage(self, miles):
        if miles >= self.mileage:
            self.mileage = miles
        else:
            print("Error: Mileage cannot decrease")

# Create an instance of the Car
my_car = Car("Toyota", "Corolla", 2022)
print(type(my_car))

# Print details of my_car
print(my_car.describe())  # Outputs: 2022 Toyota Corolla

# Update and print mileage
my_car.update_mileage(15000)
print(f"Mileage: {my_car.mileage} miles")  # Outputs: Mileage: 15000 miles


### Explanation:

# - Class: `Car` is a class, which is like a blueprint for creating objects (instances).
# - Attributes:
#   - `make`, `model`, and `year` are attributes stored within each `Car` object.
#      They define the characteristics of the car.
#   - `mileage` is an additional attribute used to track the car's mileage.

# - Methods:
#   - `describe()` is a method that uses the car's attributes to return a formatted string
#      describing the car.
#   - `update_mileage(miles)` is a method to update the car's mileage. It includes a check
#      to ensure that mileage does not decrease.

# - Instances: `my_car` is an instance of the `Car` class, representing a specific car.
#   - `__init__()`: This special method is called the initializer. It initializes new
#     instances of the class. It's automatically invoked when a new object is created.
#   - `self`: It refers to the current instance of the class. It is used to access variables
#      that belong to the class. It must be the first parameter of any method in the class.


# Study Drills :
# 1. Try creating class without init method
# 2. Create class with init method, find out the difference
# 3. Print Car details manually, later create function to display car details
# 4. Try to run display method without self
# 5. Try to call method with Syntax : Class.method(instance)