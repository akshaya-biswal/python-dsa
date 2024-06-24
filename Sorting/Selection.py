# Select first element as minimum
# Compare minimum with the remaining elements
# Swap the first with minimum


def selection_sort(array):
    size = len(array)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i

        # Swap min_idx with step
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
selection_sort(data)
print(data)

# Time Complexity: O(n*2)
# Space Complexity: O(1)
