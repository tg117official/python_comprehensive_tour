### Study Drills
#
# Add New Attributes and Methods
#    - Task: Extend the `Car` class by adding new attributes such as `color` and
#    `engine_type` (e.g., 'diesel', 'petrol', 'electric'). Add these attributes to
#    the `__init__` method and ensure they are printed in the `describe()` method.

class Car:
    def __init__(self, make, model, year, color, engine_type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_type = engine_type
        self.mileage = 0

    def describe(self):
        return f"{self.year} {self.make} {self.model}, Color: {self.color}, Engine: {self.engine_type}"

    # Input Validation in Methods
    #    - Task: Modify the `update_mileage()` method to include input validation. Ensure that the
    #            method only accepts positive integers and provides an error message if invalid
    #            input is provided.

    def update_mileage(self, miles):
        if isinstance(miles, int) and miles >= self.mileage:
            self.mileage = miles
        else:
            print("Error: Please enter a positive integer and mileage cannot decrease")

    # Add a Class Method
    #    - Task: Add a class method `from_string()` that takes a single string containing a car's
    #      details (e.g., "Toyota Corolla 2022 White Petrol"), parses the string, and returns a
    #      new instance of the class.

    @classmethod
    def from_string(cls, car_string):
        make, model, year, color, engine_type = car_string.split()
        return cls(make, model, int(year), color, engine_type)
    # A `@classmethod` is a decorator in Python that allows a method to be bound to the class
    # rather than its instance, enabling it to be called on the class itself, not just on
    # instances of the class.

    # Implement a Method to Display Status
    #    - Task: Create a method named `display_status()` in the `Car` class that prints out all
    #            the current details of the car, including its mileage.

    def display_status(self):
        print(f"Details: {self.describe()}")
        print(f"Mileage: {self.mileage} miles")

# Create Multiple Instances
#    - Task: Create multiple instances of the `Car` class with different values for make,
#            model, year, color, and engine type. Then have them use the `describe()` and
#            `display_status()` methods to print details of each car.

car1 = Car("Toyota", "Corolla", 2022, "White", "Petrol")
car2 = Car("Ford", "Mustang", 2021, "Red", "Petrol")

# car1.display_status()
# car2.display_status()
# print(car1.__dict__)
# print(car2.__dict__)
# print(Car.__dict__)

# 6. Interactive Test Script
#    - Task: Write a small interactive script where users input car details, create a `Car`
#            instance, and then can update mileage or print the car's status.

def main():
    print("Enter car details (make model year color engine_type):")
    details = input()
    car = Car.from_string(details)
    print("Enter new mileage:")
    mileage = int(input())
    car.update_mileage(mileage)
    car.display_status()

if __name__ == "__main__":
    main()

