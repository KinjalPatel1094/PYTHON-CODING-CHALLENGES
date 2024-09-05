# python program to find fibonacci series upto a given number range

# The first two numbers in the sequence are 0 and 1.
# Each subsequent number is the sum of the two previous numbers.


def find_fibonacci_series(num):
    fibonacci_result = []
    a, b = 0, 1

    while a <= num:
        fibonacci_result.append(a)
        a, b = b, a + b
    return fibonacci_result


number = 20
print(f"Fibonacci series upto {number}: {find_fibonacci_series(number)}")
