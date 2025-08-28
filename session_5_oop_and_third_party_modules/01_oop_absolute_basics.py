# ============================================================
# OOP BASICS — 20 Exercises (with solutions)
# ============================================================
from abc import ABC, abstractmethod

# ------------------------------------------------------------
# Ex1: Class & Instance — create a simple class and object
# Problem: Define Student with instance vars name, roll; print them.
# ------------------------------------------------------------
class Student:
    def __init__(self, name, roll):
        self.name = name        # instance variable
        self.roll = roll        # instance variable

s1 = Student("Asha", 101)
print("Ex1:", s1.name, s1.roll)  # Expected: Asha 101


# ------------------------------------------------------------
# Ex2: Class variable vs Instance variable
# Problem: Define Car with class var wheels=4; each car has its own color.
# ------------------------------------------------------------
class Car:
    wheels = 4                 # class variable (shared)
    def __init__(self, color):
        self.color = color     # instance variable

c1 = Car("red"); c2 = Car("blue")
print("Ex2:", c1.color, c2.color, Car.wheels, c1.wheels, c2.wheels)


# ------------------------------------------------------------
# Ex3: Instance method
# Problem: Add greet() that uses instance data.
# ------------------------------------------------------------
class Greeter:
    def __init__(self, name):
        self.name = name
    def greet(self):                      # instance method
        return f"Hello, {self.name}!"

g = Greeter("Riya")
print("Ex3:", g.greet())  # Expected: Hello, Riya!


# ------------------------------------------------------------
# Ex4: Class method (alternative constructor)
# Problem: Create from_string "name,roll" -> Student2(name, roll:int)
# ------------------------------------------------------------
class Student2:
    def __init__(self, name, roll):
        self.name = name; self.roll = roll
    @classmethod
    def from_string(cls, text):          # class method
        name, roll = text.split(",")
        return cls(name.strip(), int(roll.strip()))

s2 = Student2.from_string("Aman, 203")
print("Ex4:", s2.name, s2.roll)


# ------------------------------------------------------------
# Ex5: Static method (utility, no self/cls)
# Problem: Convert Celsius to Fahrenheit without touching instance/class.
# ------------------------------------------------------------
class TempUtil:
    @staticmethod
    def c_to_f(c):                         # static method
        return (c * 9/5) + 32

print("Ex5:", TempUtil.c_to_f(25))  # Expected: 77.0


# ------------------------------------------------------------
# Ex6: Encapsulation (convention: single underscore)
# Problem: Balance marked "protected" by convention; use methods to change it.
# ------------------------------------------------------------
class Wallet:
    def __init__(self):
        self._balance = 0   # by convention: internal
    def deposit(self, amt):
        if amt > 0: self._balance += amt
    def withdraw(self, amt):
        if 0 < amt <= self._balance: self._balance -= amt
    def show(self):
        return self._balance

w = Wallet(); w.deposit(100); w.withdraw(30)
print("Ex6:", w.show())  # Expected: 70


# ------------------------------------------------------------
# Ex7: Encapsulation with "private" + property
# Problem: Make __pin private (name-mangled). Expose balance via property with validation.
# ------------------------------------------------------------
class BankAccount:
    def __init__(self, acc_no, pin, balance=0):
        self.acc_no = acc_no
        self.__pin = pin              # private (name-mangled)
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value
    def check_pin(self, pin):
        return pin == self.__pin

ba = BankAccount("SB-001", 1234, 500)
ba.balance = 650
print("Ex7:", ba.acc_no, ba.balance, ba.check_pin(1234))


# ------------------------------------------------------------
# Ex8: Single Inheritance + overriding
# Problem: Animal.speak(); Dog overrides speak().
# ------------------------------------------------------------
class Animal:
    def speak(self):
        return "Some sound..."
class Dog(Animal):
    def speak(self):
        return "Woof!"

d = Dog()
print("Ex8:", d.speak())  # Expected: Woof!


# ------------------------------------------------------------
# Ex9: Multilevel Inheritance
# Problem: Vehicle -> Car2 -> ElectricCar adds battery_kwh.
# ------------------------------------------------------------
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
class Car2(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
class ElectricCar(Car2):
    def __init__(self, brand, model, battery_kwh):
        super().__init__(brand, model)
        self.battery_kwh = battery_kwh

ev = ElectricCar("Tata", "Nexon", 40)
print("Ex9:", ev.brand, ev.model, ev.battery_kwh)


# ------------------------------------------------------------
# Ex10: Multiple Inheritance (mixins)
# Problem: Flyer + Swimmer -> Duck can both fly and swim.
# ------------------------------------------------------------
class Flyer:
    def fly(self): return "flying"
class Swimmer:
    def swim(self): return "swimming"
class Duck(Flyer, Swimmer):
    def speak(self): return "quack"

du = Duck()
print("Ex10:", du.fly(), du.swim(), du.speak())


# ------------------------------------------------------------
# Ex11: Hierarchical Inheritance
# Problem: Shape -> Circle/Rectangle (siblings) compute area.
# ------------------------------------------------------------
class Shape:
    pass
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r * self.r
class Rectangle(Shape):
    def __init__(self, w, h): self.w = w; self.h = h
    def area(self): return self.w * self.h

print("Ex11:", round(Circle(2).area(), 2), Rectangle(3,4).area())


# ------------------------------------------------------------
# Ex12: Hybrid Inheritance (combo: multi + multilevel)
# Problem: Person -> Student3; also Worker mixin; Graduate(Student3, Worker).
# ------------------------------------------------------------
class Person:
    def __init__(self, name): self.name = name
class Student3(Person):
    def __init__(self, name, roll):
        super().__init__(name); self.roll = roll
class Worker:
    def work(self): return "working"
class Graduate(Student3, Worker):  # hybrid (inherits Student3 + Worker)
    def __init__(self, name, roll, year):
        super().__init__(name, roll); self.year = year

gr = Graduate("Meera", 501, 2025)
print("Ex12:", gr.name, gr.roll, gr.year, gr.work())


# ------------------------------------------------------------
# Ex13: Polymorphism (duck typing)
# Problem: make_it_speak(x) calls .speak() regardless of type.
# ------------------------------------------------------------
class Cat:
    def speak(self): return "meow"
class Robot:
    def speak(self): return "beep"

def make_it_speak(x):
    return x.speak()

print("Ex13:", make_it_speak(Cat()), make_it_speak(Robot()))  # meow beep


# ------------------------------------------------------------
# Ex14: Polymorphism (overriding + same interface)
# Problem: Iterate over different Animal types and call .speak().
# ------------------------------------------------------------
class Cow(Animal):
    def speak(self): return "moo"
animals = [Dog(), Cow(), Animal()]
print("Ex14:", [a.speak() for a in animals])  # ['Woof!', 'moo', 'Some sound...']


# ------------------------------------------------------------
# Ex15: Polymorphism via operator overloading
# Problem: Define Vector2D with __add__ so v1+v2 works.
# ------------------------------------------------------------
class Vector2D:
    def __init__(self, x, y): self.x = x; self.y = y
    def __add__(self, other):               # operator overloading
        return Vector2D(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

v1 = Vector2D(1,2); v2 = Vector2D(3,4)
print("Ex15:", v1 + v2)  # Expected: Vector2D(4, 6)


# ------------------------------------------------------------
# Ex16: Abstraction (ABC + abstractmethod)
# Problem: Payment base class requires pay(); subclasses implement it.
# ------------------------------------------------------------
class Payment(ABC):
    @abstractmethod
    def pay(self, amount): ...
class CashPayment(Payment):
    def pay(self, amount): return f"Cash paid: ₹{amount}"
class CardPayment(Payment):
    def pay(self, amount): return f"Card charged: ₹{amount}"

p1 = CashPayment(); p2 = CardPayment()
print("Ex16:", p1.pay(500), "|", p2.pay(750))


# ------------------------------------------------------------
# Ex17: Class variables (count instances) + classmethod
# Problem: Count how many Book objects created; get via class method.
# ------------------------------------------------------------
class Book:
    _count = 0                     # class variable
    def __init__(self, title):
        self.title = title
        Book._count += 1
    @classmethod
    def count(cls):
        return cls._count

b1 = Book("A"); b2 = Book("B"); b3 = Book("C")
print("Ex17:", Book.count())  # Expected: 3


# ------------------------------------------------------------
# Ex18: Static method for validation (used in __init__)
# Problem: Validate age is >= 0 using a staticmethod.
# ------------------------------------------------------------
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = self.validate_age(age)
    @staticmethod
    def validate_age(age):
        if age < 0: raise ValueError("Age cannot be negative.")
        return age

p = Person2("Arun", 30)
print("Ex18:", p.name, p.age)


# ------------------------------------------------------------
# Ex19: Encapsulation + name-mangling demo
# Problem: Show that __secret isn't directly accessible, but exists as _Class__secret.
# ------------------------------------------------------------
class SecretBox:
    def __init__(self):
        self.__secret = "top-secret"
    def reveal(self, key):
        return self.__secret if key == "letmein" else "nope"

box = SecretBox()
# print(box.__secret)                 # would raise AttributeError
print("Ex19:", box.reveal("letmein"))
# Access via name-mangling (not recommended, for demo only):
print("Ex19 (mangled):", box._SecretBox__secret)


# ------------------------------------------------------------
# Ex20: Polymorphism “overloading style” via default args
# Problem: same method name behave differently based on provided args count.
# ------------------------------------------------------------
class Printer:
    def show(self, a=None, b=None):
        if a is None and b is None:
            return "nothing to print"
        elif b is None:
            return f"one: {a}"
        else:
            return f"two: {a}, {b}"

pr = Printer()
print("Ex20:", pr.show(), "|", pr.show("hello"), "|", pr.show("x", 42))
