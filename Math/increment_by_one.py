# python program : You are given a large integer represented as an integer array digits, where each digits[i] is the
# ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting
# array of digits.

def plusOne(digits):
    # Start from the last digit

    # range(start,stop,step) here it starts from last index to first index in reverse order.
    for i in range(len(digits) - 1, -1, -1):
        # Add one to the current digit
        digits[i] += 1
        # If the result is less than 10, no carry, just return the result
        if digits[i] < 10:
            return digits
        # If the result is 10, set the current digit to 0 and continue
        digits[i] = 0

    # If we exit the loop, it means all digits were 9 and we have an extra carry
    # We need to add a new digit 1 at the beginning
    return [1] + digits


# Example usage:
digits = [1, 2, 3]
print(plusOne(digits))  # Output: [1, 2, 4]

digits = [9, 9, 9]
print(plusOne(digits))  # Output: [1, 0, 0, 0]
