import importlib

def main():
    # Dynamic imports
    arithmetic = importlib.import_module("math_operations.arithmetic")
    geometry = importlib.import_module("math_operations.geometry")
    descriptive = importlib.import_module("statistics_operations.descriptive")

    # Using dynamically imported modules
    print("Addition:", arithmetic.add(5, 3))
    print("Area of Circle:", geometry.area_of_circle(7))

    data = [10, 20, 30, 40]
    print("Mean:", descriptive.mean(data))

if __name__ == "__main__":
    main()
