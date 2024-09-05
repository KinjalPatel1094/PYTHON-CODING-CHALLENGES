#  python program to search element in an array.

# Binary search method , use 2 pointers.
def find_element_index(nums, target_value):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_index = (left + right) // 2

        if nums[mid_index] == target_value:
            return mid_index
        elif nums[mid_index] > target_value:
            right = mid_index - 1
        else:
            left = mid_index + 1

    # If the loop completes without finding the target,
    # the left pointer will be at the index where the target should be inserted to maintain sorted order.
    return left


arr = [1, 3, 5, 6]
target = 5
print(find_element_index(arr, target))

target = 2
print(find_element_index(arr, target))

target = 7
print(find_element_index(arr, target))

target = 0
print(find_element_index(arr, target))
