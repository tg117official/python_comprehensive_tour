# for multiple function imports
from arithmetic import add, sub, mult, div
# from stats import union_sets


def greet():
    print("Welcome to the calculations app....")


if __name__ == '__main__' :
    print(add(5, 10))
    print(sub(5, 10))
    print(mult(5, 10))
    print(div(5, 10))
    # print(union_sets({1, 2, 3}, {4, 5, 6}))
