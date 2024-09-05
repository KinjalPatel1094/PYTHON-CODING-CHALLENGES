#  python program to print unique characters.

def print_unique_characters(s):
    # Edge Case: Handle None or empty strings
    if s is None or len(s) == 0:
        return "No unique characters."

    # Create a dictionary to count occurrences of each character
    char_count = {}

    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Print characters that appear exactly once
    unique_chars = []

    for char, count in char_count.items():
        if count == 1:
            unique_chars.append(char)

    if unique_chars:
        print("Unique characters:", unique_chars)
    else:
        print("No unique characters.")


string = "character"
print_unique_characters(string)
