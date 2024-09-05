# python program to find common elements between 2 arrays.

def find_common_elements(arr1, arr2):
    # Initialize an empty list to add common elements between 2 arrays.
    common_elements = []

    for element in arr1:
        if element in arr2:
            common_elements.append(element)

    return common_elements


array1 = [1, 22, 10, 12, 55]
array2 = [42, 55, 6, 70, 10]

elements = find_common_elements(array1, array2)

print("Common elements:", elements)
