#  python program to find missing number in an array.

def find_missing_number(arr):
    n = len(arr) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2  # Sum of the first n natural numbers
    actual_sum = sum(arr)  # Sum of numbers in the array
    missing_no = expected_sum - actual_sum  # The difference gives the missing number
    return missing_no


array = [1, 2, 3, 4, 6, 7]
missing_number = find_missing_number(array)
print("Missing number is:", missing_number)
