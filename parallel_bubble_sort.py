import threading
import itertools
from typing import List

from helpers import execution_timer


def bubble_sort(array: List[int]) -> None:
    array_items_count = len(array)

    for i in range(array_items_count):
        swapped = False
        for j in range(0, array_items_count - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break


@execution_timer
def parallel_bubble_sort(*, array: List[int], threads_count: int = 4) -> List[int]:
    biggest_array_element = max(array)

    split_factor = biggest_array_element // threads_count

    sub_arrays = [[] for _ in range(threads_count)]

    for sub_array_index in range(1, len(sub_arrays)):
        for element in array:
            if element <= (split_factor * sub_array_index):
                sub_arrays[sub_array_index - 1].append(element)
                array = [new_element for new_element in array if new_element != element]

        sub_arrays[-1] = array

    active_threads = []
    for sub_array in sub_arrays:
        thread = threading.Thread(target=bubble_sort, args=(sub_array,))
        thread.start()
        active_threads.append(thread)

    for thread in active_threads:
        thread.join()

    return list(itertools.chain(*sub_arrays))
