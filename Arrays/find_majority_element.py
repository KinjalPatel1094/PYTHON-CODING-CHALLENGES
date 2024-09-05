# python program:  Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


def majorityElement(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

        # Since the problem says a majority element exists,
        # we can check if the current element is the majority.
        if counts[num] > len(nums) // 2:
            return num


# Example usage:
nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))

nums = [3, 3, 4]
print(majorityElement(nums))
