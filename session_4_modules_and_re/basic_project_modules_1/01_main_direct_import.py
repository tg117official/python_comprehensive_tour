import math_operations.arithmetic
import math_operations.geometry
import statistics_operations.descriptive
import statistics_operations.advanced

def main():
    # Using arithmetic module
    print("Addition:", math_operations.arithmetic.add(5, 3))
    print("Subtraction:", math_operations.arithmetic.subtract(5, 3))

    # Using geometry module
    print("Area of Circle:", math_operations.geometry.area_of_circle(7))

    # Using statistics modules
    data = [10, 20, 30, 40]
    print("Mean:", statistics_operations.descriptive.mean(data))
    print("Variance:", statistics_operations.advanced.variance(data))

if __name__ == "__main__":
    main()
