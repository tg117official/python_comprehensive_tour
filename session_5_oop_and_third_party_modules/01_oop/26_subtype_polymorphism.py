# 3. Subtype Polymorphism (Inheritance Polymorphism)
#       In this example, we have a base class Employee and two subclasses Developer and Manager
#       that inherit from it.

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        raise NotImplementedError("Subclasses must implement abstract method")

class Developer(Employee):
    def work(self):
        return f"{self.name} is writing code."

class Manager(Employee):
    def work(self):
        return f"{self.name} is managing the team."

def print_work(employee):
    print(employee.work())

# Example usage
dev = Developer("Alice")
mgr = Manager("Bob")

print_work(dev)  # Outputs: Alice is writing code.
print_work(mgr)  # Outputs: Bob is managing the team.
