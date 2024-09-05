# python program to find first and last element of arraylist.

def first_and_last_elements(arr):
    if len(arr) == 0:
        return None, None  # Edge case: Empty list
    elif len(arr) == 1:
        return arr[0], arr[0]  # Edge case: Single element list
    else:
        return arr[0], arr[-1]  # General case: Multiple elements


array = [10, 20, 30, 40, 50]

# Find first and last elements
first_element, last_element = first_and_last_elements(array)

print("First element:", first_element)
print("Last element:", last_element)
