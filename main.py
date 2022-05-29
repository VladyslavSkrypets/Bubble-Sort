from helpers import generate_array
from classic_bubble_sort import classic_bubble_sort


def main():
    elements_array_count = [1000, 10_000, 100_000, 1_000_000, 10_000_000]
    elements_array_count = [1000, 10_000, 100_000]

    for elements_count in elements_array_count:
        unsorted_array = generate_array(length=elements_count)
        classic_bubble_sort(array=unsorted_array)


if __name__ == '__main__':
    main()
