# python program to give output a2b2c3d2 for the input string str = aabbcccdd.

def compress_string(s):
    if not s:  # Edge case: empty string
        return "empty string"

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1  # Reset the count for the new character

    #   # Add the last character and its count
    compressed.append(s[-1] + str(count))

    return ''.join(compressed)


# Test cases
input_string = "aabbcccdd"
output_string = compress_string(input_string)
print(f"Input: {input_string}")
print(f"Output: {output_string}")
