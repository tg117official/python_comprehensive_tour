from abc import ABC, abstractmethod

# Define an abstract base class for Employee
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass
    # It is possible to add code to an abstract method in an abstract base class, and still
    # require subclasses to override it. The code in the abstract method can be executed
    # when subclasses explicitly call the method of the superclass using super(). This can be
    # useful when you want to provide some common functionality in the abstract method, which
    # subclasses can then extend or modify.

    # Concrete Method
    def say_hello(self):
        print("Hello")

# Define concrete subclasses for different types of employees
class Manager(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class Engineer(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Salesperson(Employee):
    def __init__(self, name, sales_amount, commission_rate):
        super().__init__(name)
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    def calculate_salary(self):
        return self.sales_amount * self.commission_rate

# Create instances of different types of employees
manager = Manager("John Doe", 5000)
engineer = Engineer("Alice Smith", 30, 160)
salesperson = Salesperson("Bob Johnson", 10000, 0.1)

# Calculate and print the monthly salary for each employee
print(f"{manager.name}'s monthly salary: ${manager.calculate_salary()}")
print(f"{engineer.name}'s monthly salary: ${engineer.calculate_salary()}")
print(f"{salesperson.name}'s monthly salary: ${salesperson.calculate_salary()}")

