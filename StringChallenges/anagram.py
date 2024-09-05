# python program to determine if 2 strings are anagrams.

# Two strings are anagrams if they contain the same characters in the same frequency but arranged differently.

def are_anagrams(str1, str2):

    # Edge Case: Handle None or empty strings
    # None is not a string, it's a special type in Python that represents the absence of a value.
    #  If either str1 or str2 is None , they can't be anagrams.
    if str1 is None or str2 is None:
        return False
    if len(str1) == 0 and len(str2) == 0:
        return True

    # update the strings by removing spaces and converting to lowercase
    updated_str1 = ''.join(sorted(str1.replace(" ", "").lower()))
    updated_str2 = ''.join(sorted(str2.replace(" ", "").lower()))

    # Check if the sorted versions of the strings are the same
    return updated_str1 == updated_str2


test_cases = [
    ("listen", "silent"),  # Anagrams
    ("", ""),  # Edge case: Both empty strings
    ("a", ""),  # Edge case: One empty string
    (None, "abc"),  # Edge case: One string is None
    ("HELLO", " oll eh "),  # Anagrams with extra space

]

for i, (string1, string2) in enumerate(test_cases, 1):
    result = are_anagrams(string1, string2)
    print(f"Test Case {i}: '{string1}' and '{string2}' are anagrams? :  '{result}'")
