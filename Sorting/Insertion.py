# We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater than the card in hand, it is placed on the right otherwise, to the left.
# In the same way, other unsorted cards are taken and put in their right place.
# https://www.youtube.com/watch?v=R_wDA-PmGE4&ab_channel=FelixTechTips


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            # Swap j-1 with j
            (array[j - 1], array[j]) = (array[j], array[j - 1])
            j -= 1


data = [2, 6, 5, 1, 3, 4]
insertion_sort(data)
print(data)

# Time Complexity: O(n*2)
# Space Complexity: O(1)
