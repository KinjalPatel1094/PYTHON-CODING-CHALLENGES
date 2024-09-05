# python program to swap 2 strings without using 3rd variable.

def swap_strings(str1, str2):
    # Edge case: Handle None input
    if str1 is None or str2 is None:
        print("One or both strings are None.")
        return

    print(f"Before swapping: str1 = '{str1}', str2 = '{str2}'")

    # Swapping the strings without using a third variable
    str1, str2 = str2, str1

    print(f"After swapping: str1 = '{str1}', str2 = '{str2}'")


# Test cases
print("Test Case 1: Identical strings")
swap_strings("test", "test")

print("\nTest Case 2: One string is empty")
swap_strings("python", "")

print("\nTest Case 3: Both strings are empty")
swap_strings("", "")

print("\nTest Case 4: One string is None")
swap_strings(None, "quality")
