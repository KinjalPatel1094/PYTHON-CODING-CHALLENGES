# python program to count number of words in string.

def count_words(input_string):
    # Edge case: if the string is empty, return 0
    if not input_string.strip():
        return 0

    # Strip leading/trailing whitespace and split the string by spaces
    words = input_string.strip().split()

    return len(words)


test_cases = [
    "",
    "    ",
    "kinjal",
    "Hello world!",
    "  kinjal   patel  ",
    "This is new string.",
    "QA\nEngineer",
    "using\ttab",
]

for test in test_cases:
    word_count = count_words(test)
    print(f"'{test}' -> Number of words: {word_count}")
