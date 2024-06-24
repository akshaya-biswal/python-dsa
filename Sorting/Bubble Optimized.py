# Explain:
# In the above algorithm, all the comparisons are made even if the array is already sorted.
# To solve this, we can introduce an extra variable swapped. The value of swapped is set true if there occurs swapping of elements. Otherwise, it is set false.
# After an iteration, if there is no swapping, the value of swapped will be false. This means elements are already sorted and there is no need to perform further iterations.


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
