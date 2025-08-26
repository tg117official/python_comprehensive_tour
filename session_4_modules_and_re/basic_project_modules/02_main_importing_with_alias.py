import math_operations.arithmetic as ar
import math_operations.geometry as geo
import statistics_operations.descriptive as desc
import statistics_operations.advanced as adv

def main():
    # Using arithmetic module with alias
    print("Addition:", ar.add(5, 3))
    print("Subtraction:", ar.subtract(5, 3))

    # Using geometry module with alias
    print("Area of Circle:", geo.area_of_circle(7))

    # Using statistics modules with alias
    data = [10, 20, 30, 40]
    print("Mean:", desc.mean(data))
    print("Variance:", adv.variance(data))

if __name__ == "__main__":
    main()
