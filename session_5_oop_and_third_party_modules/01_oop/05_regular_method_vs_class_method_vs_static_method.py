class GameCharacter:
    total_characters = 0  # Class variable to track the number of characters created

    def __init__(self, name, level):
        self.name = name  # Instance variable for the character's name
        self.level = level  # Instance variable for the character's level
        GameCharacter.total_characters += 1  # Increment the class variable

    # Regular method: Used to display character details
    def display_character(self):
        print(f"{self.name} is at level {self.level}.")

    # Class method: Used to create an instance of gameCharacter class
    # @classmethod
    # def from_string(cls, gameCharStr):
    #     name, level = gameCharStr.split('-')
    #     return cls(name,level)

    @classmethod
    def reset_count(cls):
        cls.total_characters = 0


    # Static method: Used to determine if a level upgrade is allowed
    @staticmethod
    def can_level_up(experience_points):
        return experience_points >= 1000

# Create instances of GameCharacter
character1 = GameCharacter("Link", 5)
character2 = GameCharacter("Zelda", 7)


# Call class method: it affects class state, not dependent on any instance
# newGameChar1 = 'crimson-11'
# character3 = GameCharacter.from_string(newGameChar1)
# character3.display_character()

# Call static method: performs a utility task, checking if a level can be upgraded
print(GameCharacter.can_level_up(1200))  # Outputs: True
print(GameCharacter.can_level_up(800))   # Outputs: False
print(character1.can_level_up(1500))

# Call instance method
print(GameCharacter.display_character(character2))
print(character1.display_character())
print(character2.display_character())

# Printing Value for class variable
print(GameCharacter.total_characters)
print(character1.total_characters)
print(character2.total_characters)

# calling class method
GameCharacter.reset_count()
character1.reset_count()
character2.reset_count()

print(GameCharacter.total_characters)
print(character1.total_characters)
print(character2.total_characters)


# Regular Method/ Instance Method (display_character):
#       Uses self to access and display instance-specific data such as the character's
#       name and level.
# Class Method (from_string):
#       Uses cls to access and manipulate data related to the class as a whole, like the total
#       number of game characters created. Useful for actions that affect the entire class rather
#       than individual instances.
# Static Method (can_level_up):
#       Does not need access to either instance-specific data or class-specific data. It simply
#       provides utility functionality to determine if a character can level up based on
#       experience points, making it completely independent of the character's state.


# Study Drills :
# 1. Try to run class method using instances and Using class figure out the difference
# 2. Create GamePlayer from a String with and without class method


# class Employee :
#     num_emps = 0
#     incr = 1.10
#
#     def __init__(self, eid, ename, salary):
#         self.eid = eid
#         self.ename = ename
#         self.salary = salary
#         Employee.num_emps += 1
#
#     def display_info(self):
#         print(f"Emp Details : {self.eid}, {self.ename}, {self.salary}")
#
#     def incr_salary(self):
#         self.salary = self.salary*Employee.incr
#
#     @classmethod
#     def update_incr(cls, inc):
#         cls.incr = inc
#
#     @classmethod
#     def reset_emp_count(cls):
#         cls.num_emps = 0
#
# emp1 = Employee(1, "abc", 4.5)
# emp2 = Employee(2, "xyz", 4.7)
#
# emp1.display_info()
# emp2.display_info()
#
# emp1.incr_salary()
# print("After Incrementing Salary of emp1")
# emp1.display_info()
#
# Employee.update_incr(1.15)
# print(f"Increment has been update to {Employee.incr}")
#
# emp2.incr_salary()
# print("After Incrementing Salary of emp2")
# emp2.display_info()

