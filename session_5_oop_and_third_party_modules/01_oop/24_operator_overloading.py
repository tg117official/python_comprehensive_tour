# Ad-Hoc Polymorphism (Operator Overloading)
#   In this example, we'll overload the + operator to add custom Money objects.

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount, 'USD')
        return NotImplemented

    def __str__(self):
        return f"${self.amount:.2f}"

# Example usage
wallet1 = Money(50, 'USD')
wallet2 = Money(75, 'USD')
total = wallet1 + wallet2  # Uses the overloaded + operator
print(total)  # Outputs: $125.00
