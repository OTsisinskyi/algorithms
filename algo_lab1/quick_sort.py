import datetime
import sys

comparisons = 0
swaps = 0


def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]
    global swaps
    swaps += 1


def partition(array_for_quicksort, start, end):
    pivot = array_for_quicksort[start]
    low = start + 1
    high = end

    global comparisons
    comparisons += 1
    while True:
        while low <= high and array_for_quicksort[high] >= pivot:
            high = high - 1

        while low <= high and array_for_quicksort[low] <= pivot:
            low = low + 1

        if low <= high:
            swap(low, high, array_for_quicksort)
        else:
            break

    swap(start, high, array_for_quicksort)

    return high


def quick_sort(array_for_quicksort, start, end, order):
    if start >= end:
        return
    pi = partition(array_for_quicksort, start, end)
    quick_sort(array_for_quicksort, start, pi - 1, order)  # left partition
    quick_sort(array_for_quicksort, pi + 1, end, order)  # right partition

    if order == "asc":
        return array_for_quicksort
    elif order == "desc":
        return array_for_quicksort.reverse()


if __name__ == '__main__':
    enter_array = sys.argv[1:-1]
    enter_asc_or_desc = sys.argv[-1]
    ready_array = [int(i) for i in enter_array]
    start_time = datetime.datetime.now()
    quick_sort(ready_array, 0, len(ready_array) - 1, enter_asc_or_desc)
    time_sort = datetime.datetime.now() - start_time
    print("QuickSort: \n"
          f"Execution time: {time_sort.total_seconds() * 1000:.2f} ms\n"
          f"Comparisons: {comparisons} \n"
          f"Swaps: {swaps} \n"
          f"Sorted array: {ready_array}")