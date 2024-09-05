# python program to give 2 output "abcde" , "ABCDE" for the input string = "aBACbcEDed".


def separate_characters(s):
    # Initialize empty strings to store the results
    lowercase_result = ""
    uppercase_result = ""

    # Use sets to track characters that have already been added
    lower_chars = set()
    upper_chars = set()

    for char in s:

        lower_char = char.lower()
        upper_char = char.upper()
        if lower_char not in lower_chars:
            lowercase_result += lower_char
            lower_chars.add(lower_char)
        elif upper_char not in upper_chars:
            uppercase_result += upper_char
            upper_chars.add(upper_char)

    return lowercase_result, uppercase_result


# Test the function
input_string = "aBACbcEDed"
lowercase_output, uppercase_output = separate_characters(input_string)
print(f"Input: {input_string}")
print(f"Lowercase Output: {lowercase_output}")
print(f"Uppercase Output: {uppercase_output}")
