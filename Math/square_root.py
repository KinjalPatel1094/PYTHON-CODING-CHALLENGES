#  Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
#  The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.

# implementing a binary search algorithm to find the square root.
def mySqrt(x):
    if x < 2:
        return x

    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared < x:
            low = mid + 1
        else:
            high = mid - 1

    return high


test_cases = [0, 1, 4, 8, 16, 25, 100]
for num in test_cases:
    print(f"The square root of {num} is {mySqrt(num)}")
