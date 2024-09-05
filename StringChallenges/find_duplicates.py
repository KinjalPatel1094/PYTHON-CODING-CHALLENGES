# python program to find duplicate character in string.

from collections import Counter


def find_duplicates(original_str):
    # edge case
    if not original_str:
        return "Input string is empty"

    # Count the frequency of each character in the string
    char_count = Counter(original_str)

    # Initialize an empty dictionary to hold duplicates
    duplicate_chars = {}

    # items() method returns an iterable of key-value pairs.
    for char, count in char_count.items():
        if count > 1:
            duplicate_chars[char] = count

    # Edge case: No duplicates found
    if not duplicate_chars:
        return "No duplicate characters found"

    return duplicate_chars


input_strings = ["aabbcc", "HelLo", "", "112233@@&&", "    ", "PROGRAMME", "ABCD" , "p"]

for input_string in input_strings:
    print(f"input: {input_string}")
    output = find_duplicates(input_string)
    print(f"output: {output}")
