# python program to find if string is palindrome.

def is_palindrome(string):
    # Edge case: empty string is considered a palindrome
    if not string:
        return True

    # Create a list to store alphanumeric characters.
    filtered_string = []

    # Convert the string to lowercase and remove non-alphanumeric characters
    for char in string:
        if char.isalnum():
            filtered_string.append(char.lower())

    updated_string = ''.join(filtered_string)

    return updated_string == updated_string[::-1]


test_cases = [
    "",  # Edge case: Empty string
    "a",  # Single character
    "Racecar",  # Simple palindrome with mixed case
    "No lemon, no melon",  # Palindrome with spaces and punctuation
    "hello",  # Not a palindrome
    "12321",  # Numeric palindrome
    "12345",  # Not a palindrome
    "Was it a car or a cat I saw?",  # Palindrome with question mark and spaces
]

# Using 'enumerate':which is a built-in Python function that adds a counter to an iterable like list.
# The second argument 1 is the start index for the counter.
# This means the counter will start at 1 instead of the default 0.
for i in range(len(test_cases)):
    result = is_palindrome(test_cases[i])
    print(f"Test case {i+1} : {test_cases[i]} : Is Palindrome? : '{result}'")
