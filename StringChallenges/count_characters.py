# python program to count occurrence of each character in string.


def count_characters(input_string):
    char_count = {}

    # # Check for edge case: empty string
    if not input_string:
        print("input string is empty")
        return char_count

    # Convert character to lowercase to treat 'A' and 'a' as the same character
    for char in input_string:
        char = char.lower()

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


original_string = "Python string Challenge"
result = count_characters(original_string)

for char, count in result.items():
    print(f"{char} : {count}")
