# python program to sum only integers where array has special characters and integers.

def sum_integers(arr):
    total = 0
    for element in arr:

        # isinstance(object, class) is a built-in Python function,
        # that is used to check whether the variable element is an instance of the int class
        if isinstance(element, int):
            total += element
    return total


array = [1, 'a', 5, '*', 7, '$', 10, 'L', 3]

result = sum_integers(array)
print(f"The sum of integers in the array is: {result}")
