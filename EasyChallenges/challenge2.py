# Find the missing values from a sorted array.


def missing_values(arr):
    missing_numbers = []
    for i in range(arr[0], arr[-1] + 1):
        if i not in arr:
            missing_numbers.append(i)
    return missing_numbers


arr = [7, 9, 11, 15, 17, 18, 20]
print(missing_values(arr))
