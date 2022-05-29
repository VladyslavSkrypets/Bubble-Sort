from typing import List


def classic_bubble_sort(array: List[int]) -> List[int]:
    array_items_count = len(array)

    for i in range(array_items_count):
        swapped = False

        for j in range(array_items_count - i - 1):
            if array[i] > array[j + 1]:
                array[i], array[j + 1] = array[j + 1], array[i]

                swapped = True

        if not swapped:
            break

    return array
