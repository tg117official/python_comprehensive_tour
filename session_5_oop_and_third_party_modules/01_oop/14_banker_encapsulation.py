# Encapsulation is a fundamental concept in object-oriented programming (OOP) that
# involves bundling the data (attributes) and methods that operate on the data into
# a single unit or class. It restricts direct access to some of an object's components,
# which is a way of preventing direct modification of data. This is typically done by
# making some components private, which means they can only be changed by methods inside
# the class.

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to the balance")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from the balance")
        else:
            print("Invalid withdrawal amount")

    def __avg_hours_per_day(self, hours):
        self.total_hours = hours
        avg_hrs = self.total_hours / 20
        return avg_hrs

    def show_balance(self, hrs):
        print(f"Current balance: {self.__balance} and Hours are : {self.__avg_hours_per_day(hrs)}")

# Study Drills
# 1. Try to print __balance using instance
# 2. Try executing  __avg_hours_per_day using instance
# 3. Understand all instance methods by calling them
# 4. Understand the program
# 5. Create Student class | rno,name,email,marks(int), __cno |
#    | __get_grade() : Grade | display_info : rno,name,email,cno,grade |

# Creating an instance of Account
acc = Account("John")
acc.deposit(100)
acc.withdraw(50)
acc.show_balance(160)  # Outputs: Current balance: 50

# print(Account.__balance)
# print(acc.__avg_hours_per_day())

# Explanation:
# - Private Attribute: `__balance` is a private attribute (denoted by two underscores).
#       It cannot be accessed directly from outside the class, which protects its integrity
#       by hiding the data.
# - Public Methods: `deposit`, `withdraw`, and `show_balance` are public methods that provide
#       a controlled way to access and modify the private attribute `__balance`.

### Real-Life Example of Encapsulation

# Consider a real-life example of a coffee machine. A coffee machine encapsulates all
# the functionalities to make coffee. The user interacts with a simple interface
# (buttons to choose coffee type, start brewing, etc.), but the internal mechanics like
# water heating, bean grinding, and brew timing are hidden from the user.
#
# In this example:
# - Internal Mechanics: These are like private attributes/methods which users cannot directly
#                       access or modify.
# - Interface (Buttons): These are like public methods that allow the user to use the coffee
#                        machine without knowing about the complex processes happening inside.
#
# ### Why Encapsulation?
#
# Encapsulation helps to:
# - Protect the internal state of an object by preventing external components from directly
#   accessing it.
# - Reduce complexity by hiding the implementation details and exposing only what is necessary
#   to the outside world.
# - Increase reusability by keeping a clear separation between the interface and the
#   implementation.
