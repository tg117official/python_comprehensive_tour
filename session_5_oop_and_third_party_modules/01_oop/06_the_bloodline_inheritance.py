## Inheritance with Employee, Developer, and Manager

# Base class
class Employee:
    def __init__(self, name, email):
        self.name = name  # Employee name
        self.email = email  # Employee email

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")


# Derived class for developers
class Developer(Employee):
    def __init__(self, name, email, programming_lang):
        super().__init__(name, email)  # Call to the superclass (Employee) constructor
        self.programming_lang = programming_lang  # Additional attribute specific to developers

# class Developer(Employee):
#     def __init__(self, name, email, programming_lang):
#         Employee.__init__(self, name, email)

    def display_info(self):
        super().display_info()
        # Employee.display_info(self)
        print(f"Programming Language: {self.programming_lang}")


# Derived class for managers
class Manager(Employee):
    def __init__(self, name, email, emp_list=None):
        super().__init__(name, email)
        if emp_list is None:
            self.emp_list = []  # Additional attribute to store a list of employees under this manager
        else:
            self.emp_list = emp_list
    def add_emp(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)

    def display_emps(self):
        print(f"{self.name}'s team:")
        for emp in self.emp_list:
            emp.display_info()  # Display info of each employee


# Example usage
dev1 = Developer("Alice", "alice@example.com", "Python")
dev2 = Developer("Taka", "taka@example.com", "java")
mgr = Manager("Bob", "bob@example.com", [dev2, dev1])

# Adding employees under manager
# mgr.add_emp(dev)

# Display information
# dev.display_info()  # Shows developer's info including programming language
mgr.display_emps()  # Shows all employees under the manager
print(issubclass(Developer,Employee))


### Explanation:
# - `Employee` (Base class):
#   - Contains common attributes like `name` and `email` and a method `display_info()` that
#     prints the employee's information.

# - `Developer` (Derived class):
#   - Inherits from `Employee` and adds a specific attribute `programming_lang`.
#   - The `__init__` method uses `super()` to call the `Employee` class's constructor,
#     ensuring all Employee attributes are initialized.
#   - Overrides the `display_info()` method to include details about the programming language.

# - `Manager` (Derived class):
#   - Also inherits from `Employee` and includes a list `emp_list` to manage employees.
#   - `add_emp(emp)` and `remove_emp(emp)` methods to add and remove employees to/from the manager's list.
#   - `display_emps()` to print information about all employees under this manager, leveraging
#      the `display_info()` method from the `Employee` class.

