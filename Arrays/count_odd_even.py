# python program to count odd and even numbers from array

def count_odd_even(array):
    even = 0
    odd = 0

    for num in array:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count, odd_count = count_odd_even(arr)

print(f"Even numbers found in array: {even_count}")
print(f"Odd numbers found in array: {odd_count}")
