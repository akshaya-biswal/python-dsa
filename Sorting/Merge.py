def merge(left, right):
    merged = []
    i = j = 0

    # Merge the two arrays while comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[i])
            j += 1

    # If there are remaining elements in the left array, add them
    while i < len(left):
        merged.append(left[i])
        i += 1

    # If there are remaining elements in the right array, add them
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def merge_sort(array):
    if len(array) <= 1:
        return array

    # Find the middle point and divide the array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Recursively sort the halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


data = [12, 11, 13, 5, 6, 7]
sorted_data = merge_sort(data)
print(sorted_data)
