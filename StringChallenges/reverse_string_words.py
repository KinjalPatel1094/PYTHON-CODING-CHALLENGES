# python program to reverse each word of given string


def reverse_string_word(actual_string):
    # Split the sentence into words
    words = actual_string.split()

    # Check if the list is empty
    if not words:
        return ""

    # Create an empty list to hold the reversed words
    reversed_words_list = []

    # Reverse each word and add it to the list
    for word in words:
        reversed_word = word[::-1]
        reversed_words_list.append(reversed_word)

    # Join the reversed words into a single string
    reversed_words = ' '.join(reversed_words_list)

    return reversed_words


original_string = "Python Coding Challenges"
reversed_string = reverse_string_word(original_string)

print(f"Original string:{original_string}")
print(f"reversed each word in string: {reversed_string}")
