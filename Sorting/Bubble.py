# Explain:
# Compare the adjacent elements
# Put the largest element at the end

# Code:
# loop to access each array element
# loop to compare array elements


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


data = [-2, 45, 0, 11, -9]
bubble_sort(data)
print(data)
