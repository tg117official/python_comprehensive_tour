# Duck Typing (Dynamic Polymorphism)
#     In this example, we use duck typing to treat different objects uniformly as long as
#     they have a fly method.

class Airplane:
    def fly(self):
        return "The airplane is flying."

class Bird:
    def fly(self):
        return "The bird is flying."

class Kite:
    def fly(self):
        return "The kite is flying."

def let_it_fly(flyer):
    print(flyer.fly())

# Example usage
plane = Airplane()
sparrow = Bird()
kite = Kite()

let_it_fly(plane)    # Outputs: The airplane is flying.
let_it_fly(sparrow)  # Outputs: The bird is flying.
let_it_fly(kite)     # Outputs: The kite is flying.
