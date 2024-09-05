# Remove duplicate characters from a given string


def remove_duplicates(input_string):
    updated_String = ""
    # Initialize an empty set to keep track of seen characters
    # A set in Python is an unordered collection of unique elements.it is mutable.
    seen = set()

    for char in input_string:
        if char not in seen:
            seen.add(char)
            updated_String += char

    return updated_String


original_string = "balloon"
print(remove_duplicates(original_string))
