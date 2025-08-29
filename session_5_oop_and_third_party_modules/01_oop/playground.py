
# create a program
# Class :  Student
# create 3 instances/ object
# Attributes : rno, name, class
# function : print_detail


class Car:
    num_wheels = 4
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def print_details(self):
        print(self.brand, self.model, self.mileage)


car1 = Car("Tata", "Tiago", 20)
# Car.__init__(car1, "Tata", "Tiago", 20)

car2 = Car("MS", "Swift", 21)
# Car.__init__(car2, "MS", "Swift", 21)

car3 = Car("TATA", "Nexon", 18)
# Car.__init__(car3, "TATA", "Nexon", 18)


# Access using Class | Access using Instance
print(Car.num_wheels) # Using Clas
print(car1.num_wheels) # using instance

# Accessing Instance variables
print(car1.model)
# print(Car.model) won't work as using class we cannot access instance variable

# Modifying vale for instance variable
car1.model = "Altroz"
car1.print_details()

# Accessing class variable
print(Car.num_wheels)
print(car1.num_wheels)
print(car2.num_wheels)
print(car3.num_wheels)

# Modify class variable
Car.num_wheels = 8 # using Class : M --> all Instances + Class
# car1.num_wheels = 8 # using instance : M --> Instance
print("Class : ", Car.num_wheels)
print("car1 : ", car1.num_wheels)
print("car2 : ", car2.num_wheels)
print("car3 : ", car3.num_wheels)


