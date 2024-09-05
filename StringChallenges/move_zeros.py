# python program to give output "32412120000" for the input "32400121200".

def move_zeros_to_end(s):
    # Initialize strings to hold non-zero digits and zeros
    non_zero_digits = ""
    zeros = ""

    # Iterate through each character in the input string
    for char in s:
        if char == "0":
            zeros += char  # Collect zeros
        else:
            non_zero_digits += char  # Collect non-zero digits

    # Combine non-zero digits with zeros at the end
    return non_zero_digits + zeros


# Test the function
input_string = "32400121200"
output_string = move_zeros_to_end(input_string)
print(f"Input: {input_string}")
print(f"Output: {output_string}")
