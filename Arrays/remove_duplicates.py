# python program to remove duplicates from arraylist.


# converting array into set to remove duplicates and
# then back to list to return array of unique elements.
def remove_duplicates(arr):
    return list(set(arr))


array = [1, 2, 3, 4, 2, 3, 5, 6, 1]
unique_array = remove_duplicates(array)
print("Array without duplicates:", unique_array)
