# Multiple inheritance occurs when a class inherits from more than one base class.
# Care must be taken to manage the complexity and avoid conflicts, such as the diamond problem.

class Mother:
    def mothers_skills(self):
        print("Driving, Art")

class Father:
    def fathers_skills(self):
        print(f"Gardening, Programming")

class Child(Mother, Father):  # Inherits from both Father and Mother
    def skills_child(self):
        Father.fathers_skills(self)
        self.mothers_skills()
        self.fathers_skills()
# self can be used to access methods from parent classes within the child class method. This is
# done by explicitly calling the parent class method with self as the argument, like
# Father.skills(self) and Mother.skills(self). By passing self, you ensure that the
# skills method of the Father and Mother classes is called on the instance of the Child
# class.

# Usage
child = Child()
child.mothers_skills()
child.fathers_skills()
child.skills_child()
# Outputs:
# Gardening, Programming
# Cooking, Art
# Sports
