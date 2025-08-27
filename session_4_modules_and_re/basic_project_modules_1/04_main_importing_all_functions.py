from math_operations.arithmetic import *
from math_operations.geometry import *
from statistics_operations.descriptive import *
from statistics_operations.advanced import *

def main():
    # Using all imported functions
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Area of Circle:", area_of_circle(7))

    data = [10, 20, 30, 40]
    print("Mean:", mean(data))
    print("Variance:", variance(data))

if __name__ == "__main__":
    main()
