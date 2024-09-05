# python program to find the longest substring without repeating characters.

def longest_substring(s):
    # Set to store the unique characters in the current window
    char_set = set()
    # Variables to keep track of the starting index of the current window and the maximum length of the substring
    left = 0
    max_len = 0
    longest_substr = ""

    # Iterate over each character in the string using the right pointer
    for right in range(len(s)):
        # If the character is already in the set, move the left pointer to the right
        # until the character can be removed from the set
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the current character to the set
        char_set.add(s[right])

        # Calculate the length of the current window
        current_len = right - left + 1

        # Update the maximum length and the longest substring if a new maximum is found
        if current_len > max_len:
            max_len = current_len
            longest_substr = s[left:right + 1]

    return longest_substr, max_len


# Test the function
input_string = "pwwkew"
substring, length = longest_substring(input_string)
print(f"Input: {input_string}")
print(f"Longest Substring Without Repeating Characters: {substring}")
print(f"Length: {length}")
