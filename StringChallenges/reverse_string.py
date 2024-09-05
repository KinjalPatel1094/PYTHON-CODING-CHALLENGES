# python program to reverse a string.


# using Python's slicing technique, [::-1], to reverse the string.
def reverse_string(str):
    return str[::-1]


str = "kinjal patel"
reverse_str = reverse_string(str)

print(f"Original String: {str}")
print(f"Reversed String: {reverse_str}")
