# Polymorphism is a fundamental concept in object-oriented programming that allows
# methods to do different things based on the object calling them. This concept enables
# a single interface to represent different underlying forms (data types).

### Real World Scenario: Transport System

# Let's consider a transport system where various types of vehicles have a common method to
# start but behave differently based on the vehicle type. For instance, a car starts by
# turning a key, a bicycle starts by pedaling, and a boat starts by turning a throttle.

### Python Script Demonstrating Polymorphism


class Vehicle:
    def start(self):
        """A generic method to start a vehicle. To be implemented by each vehicle type."""
        pass

class Car(Vehicle):
    def start(self):
        """Starts a car by turning the ignition key."""
        print("Turning the ignition key to start the car.")

class Bicycle(Vehicle):
    def start(self):
        """Starts a bicycle by pedaling."""
        print("Pedaling to start the bicycle.")

class Boat(Vehicle):
    def start(self):
        """Starts a boat by turning the throttle."""
        print("Turning the throttle to start the boat.")

# Example usage
car = Car()
bicycle = Bicycle()
boat = Boat()

car.start()
bicycle.start()
boat.start()


### Explanation
# - Base Class (`Vehicle`):
#       This class has a method `start` which is intended to be overridden in derived classes.
#       It does not implement any functionality itself.
# - Derived Classes (`Car`, `Bicycle`, `Boat`):
#       Each of these classes represents a different type of vehicle. They each provide a
#       specific implementation of the `start` method, demonstrating how they start differently.
# - Function `start_vehicle`:
#       This function demonstrates polymorphism; it accepts any object that's a subclass of
#       `Vehicle` and calls its `start` method. Depending on the class of the object passed,
#       the appropriate `start` method is called.

### Real-Life Benefits of Polymorphism
# - Flexibility :
#       Allows you to write flexible and reusable code. For example, the `start_vehicle`
#       function can start any kind of vehicle without knowing its specific type.
# - Maintainability:
#       Simplifies system maintenance and extension as new vehicle types can be added with
#       minimal changes to existing code.
# - Interchangeability :
#       Objects of different classes can be treated interchangeably, yet behave differently when
#       invoking their methods.

