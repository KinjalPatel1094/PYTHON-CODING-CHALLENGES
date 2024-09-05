#  python program to find the largest and smallest element in array


def find_min_max(arr):
    if not arr:
        return None, None  # Return None for both min and max if array is empty

    # Initialize min and max with the first element
    min_num = max_num = arr[0]

    # Iterate through the array
    for num in arr:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    return min_num, max_num


array = [3, 1, 4, 1, 5, 9, 2]
min_element, max_element = find_min_max(array)
print("Smallest element:", min_element)
print("Largest element:", max_element)
