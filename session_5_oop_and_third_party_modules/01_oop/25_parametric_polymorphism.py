# Parametric Polymorphism (Using Generics)
#   In Python, we use dynamic typing, so we naturally use parametric polymorphism without
#   explicit generics. Here’s an example using a simple stack that can work with any data type.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

# Example usage with different data types
stack = Stack()
stack.push(1)
stack.push("apple")
stack.push([3, 4, 5])

print(stack.pop())  # Outputs: [3, 4, 5]
print(stack.pop())  # Outputs: apple
print(stack.pop())  # Outputs: 1
