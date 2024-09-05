# python program to give output "kinjal" and "123" for input "Kin12ja3l".

def separate_alpha_numeric(s):

    # Initialize empty strings to store alphabets and digits
    alphabets = ""
    digits = ""

    # Iterate through each character in the input string
    for char in s:
        if char.isalpha():
            alphabets += char
        elif char.isdigit():
            digits += char

    return alphabets, digits


# Test the function
input_string = "Kin12ja3l"
alphabet_output, digit_output = separate_alpha_numeric(input_string)
print(f"Input: {input_string}")
print(f"Alphabets: {alphabet_output}")
print(f"Digits: {digit_output}")
