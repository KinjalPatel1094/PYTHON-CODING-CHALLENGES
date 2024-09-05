# python program to print each letter twice from a given string.

def each_letter_twice(s):
    # Edge Case: Handle None or empty strings
    if s is None or len(s) == 0:
        return "Empty string - No characters"

    doubled_string = []
    # Iterate through each character in the string and print it twice

    for char in s:
        doubled_string.append(char * 2)

    return ''.join(doubled_string)


string = "A B C"
print(each_letter_twice(string))
