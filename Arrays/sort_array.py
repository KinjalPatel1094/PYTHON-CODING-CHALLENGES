# python program to sort an array without using in built method.


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example array
array = [64, 25, 12, 22, 11]
print ("given array:", array)
selection_sort(array)
print("Sorted array:", array)
