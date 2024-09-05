# python program to find all permutations of a given string.
from itertools import permutations

# It is used to generate all possible arrangements of a given sequence,
# (such as a string, list, or tuple) where the order of the elements matters.
def find_permutations(string):
    # Edge case: empty string
    if not string:
        return [""]

    # Generate all permutations of the string
    # The permutations function comes from Python's itertools module.
    # Each permutation is returned as a tuple of elements.
    # perm_list is an iterator that will generate the tuples representing the permutations of the input string.
    perm_list = permutations(string)

    perm_strings = []

    # Convert permutations from tuples to strings and remove duplicates by converting it to set.
    for perm in set(perm_list):  # Iterate through the unique permutations
        perm_strings.append(''.join(perm))  # Join the tuple into a string and add to list

    return perm_strings


test_cases = [
    "",  # Edge case: Empty string
    "a",  # Single character
    "KK",  # Repeated characters
    "kinjal",  # Distinct characters
    "css",  # Mixed repeated and distinct characters
    "html",  # Longer string with distinct characters
    "123",  # Numeric string
]

for i, test in enumerate(test_cases, 1):
    result = find_permutations(test)
    print(f"Test case {i}: '{test}' -> Permutations: {result}")
