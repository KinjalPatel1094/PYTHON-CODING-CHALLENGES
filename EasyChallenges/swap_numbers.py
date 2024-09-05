# python program to swap two numbers without using third variable.


def swap_nums(a, b):
    print(f"values of a and b before swapping:({a}, {b})")

    a = a + b
    b = a - b
    a = a - b

    return a, b


num1 = 30
num2 = 60

print("values of a and b after swapping:", swap_nums(num1, num2))
