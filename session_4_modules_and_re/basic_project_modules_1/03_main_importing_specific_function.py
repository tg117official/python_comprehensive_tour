from math_operations.arithmetic import add, subtract
from math_operations.geometry import area_of_circle
from statistics_operations.descriptive import mean
from statistics_operations.advanced import variance

def main():
    # Using specific functions directly
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))

    # Using specific geometry function
    print("Area of Circle:", area_of_circle(7))

    # Using specific statistics functions
    data = [10, 20, 30, 40]
    print("Mean:", mean(data))
    print("Variance:", variance(data))

if __name__ == "__main__":
    main()
