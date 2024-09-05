# python program to count vowels and consonants in a string

def count_vowels_and_consonants(s):
    # Define vowels
    vowels = "aeiouAEIOU"

    # Initialize counts
    vowel_count = 0
    consonant_count = 0

    # Edge Case: Handle None or empty strings
    if s is None or len(s) == 0:
        return 0, 0

    # Count vowels and consonants
    for char in s:
        if char.isalpha():  # Check if the character is an alphabetic letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


# Test cases
test_cases = [
    "alphanumeric",  # Mixed case with vowels and consonants
    "HELLO",  # Uppercase letters
    "100",  # No alphabetic characters
    "",  # Edge case: Empty string
    None,  # Edge case: None
    "aeiou",  # Only vowels
    "bcgh",  # Only consonants
    "count vowels and consonants from this string "  # Mixed case with all letters
]

for i, string in enumerate(test_cases, 1):
    vowels, consonants = count_vowels_and_consonants(string)
    print(f"Test Case {i}: '{string}' -> Vowels: {vowels}, Consonants: {consonants}")
