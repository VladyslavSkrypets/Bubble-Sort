from typing import List

from helpers import execution_timer


@execution_timer
def classic_bubble_sort(*, array: List[int]) -> List[int]:
    array_items_count = len(array)

    for i in range(array_items_count):
        swapped = False
        for j in range(array_items_count - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            break

    return array
