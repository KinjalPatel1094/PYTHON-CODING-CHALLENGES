# python program to give output "00003241212" for the input "32400121200".

def move_zeros_to_front(s):
    # Initialize strings to hold non-zero digits and zeros
    non_zero_digits = ""
    zeros = ""

    # Iterate through each character in the input string
    for char in s:
        if char == '0':
            zeros += char
        else:
            non_zero_digits += char  

    # Combine zeros with non-zero digits at the end
    return zeros + non_zero_digits

# Test the function
input_string = "32400121200"
output_string = move_zeros_to_front(input_string)
print(f"Input: {input_string}")
print(f"Output: {output_string}")
