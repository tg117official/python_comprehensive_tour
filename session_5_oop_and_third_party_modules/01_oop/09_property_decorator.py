class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Property for the email
    @property
    def email(self):
        """Generate email dynamically from first and last name."""
        return f"{self.first.lower()}.{self.last.lower()}@company.com"

    # Property for the full name
    @property
    def fullname(self):
        """Return the full name."""
        return f"{self.first} {self.last}"

    # Setter for the full name
    @fullname.setter
    def fullname(self, name):
        """Allow setting full name, which updates first and last names."""
        first, last = name.split()
        self.first = first
        self.last = last

    # Deleter for the full name
    @fullname.deleter
    def fullname(self):
        """Delete the full name and reset first and last names to None."""
        print("Deleting Name!")
        self.first = None
        self.last = None

# Example usage
emp_1 = Employee('John', 'Doe')

# Print initial email and fullname
print(emp_1.email)       # Outputs: john.doe@company.com
print(emp_1.fullname)    # Outputs: John Doe

# Change the fullname
emp_1.fullname = 'Jane Smith'

# Print updated email and fullname
print(emp_1.email)       # Outputs: jane.smith@company.com
print(emp_1.fullname)    # Outputs: Jane Smith

# Delete the fullname
del emp_1.fullname

# Attempt to print full name and email after deletion
print(emp_1.fullname)    # Outputs: None None
print(emp_1.email)       # Will error out if accessed without checking for None values

# Study Drill :
# 1. Create a Student class,
# attributes (rno, first name, last name, marks)
# methods (display info, email, fullname)
# create an instance of student, print(full_name and email_id)
# First perform without property decorator
# second time with property decorator
