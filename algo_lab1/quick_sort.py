import time
import sys
import os
#from random import randint

comparisons = 0
swaps = 0


def swap(a, b, arr):
    arr[a], arr[b] = arr[b], arr[a]
    global swaps
    swaps += 1


def partition(array_for_quicksort, start, end, order):
    pivot = array_for_quicksort[start]
    low = start + 1
    high = end

    global comparisons
    comparisons += 1
    while True:
        if order == "ASC":
            while low <= high and array_for_quicksort[high] >= pivot:
                high -= 1
            while low <= high and array_for_quicksort[low] <= pivot:
                low += 1

        elif order == "DESC":
            while low <= high and array_for_quicksort[high] <= pivot:
                high -= 1
            while low <= high and array_for_quicksort[low] >= pivot:
                low += 1
        if low <= high:
            swap(low, high, array_for_quicksort)
        else:
            break
    swap(start, high, array_for_quicksort)
    return high


def quick_sort(array_for_quicksort, start, end, order):
    if start >= end:
        return
    pi = partition(array_for_quicksort, start, end, order)
    quick_sort(array_for_quicksort, start, pi - 1, order)  # left partition
    quick_sort(array_for_quicksort, pi + 1, end, order)  # right partition


if __name__ == '__main__':
    enter_array = sys.argv[1:-1]
    enter_asc_or_desc = sys.argv[-1]
    ready_array = [int(i) for i in enter_array]

    #my_list = [randint(1, 1000) for i in range(100)]

    start_time = time.time()
    quick_sort(ready_array, 0, len(ready_array) - 1, enter_asc_or_desc)
    end_time = time.time()

    print("QuickSort: \n"
          f"Execution time: {(end_time - start_time) * 1000} ms\n"
          f"Comparisons: {comparisons} \n"
          f"Swaps: {swaps} \n"
          f"Sorted array: {ready_array}")

    command = "python -m unittest test.TestQuickSort"
    os.system(command)
