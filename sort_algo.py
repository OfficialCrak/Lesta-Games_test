import random
from typing import List

from decorator import time_it


def generate_random_array(size: int, max_abs_value: int = 1000) -> List[int]:
    return [random.randint(-max_abs_value, max_abs_value) for _ in range(size)]


#Сортировка слиянием, универсальная O(N log N)
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])

    return merge(left_list, right_list)


@time_it
def merge_sort_wrapper(arr: List[int]) -> List[int]:
    arr_copy = arr[:]
    return merge_sort(arr_copy)

###############################################

#Встроенный алгоритм сортировки в python, TimSort
@time_it
def timsort_wrapper(arr: List[int]) -> List[int]:
    arr_copy = arr[:]
    arr_copy.sort()
    return arr_copy


#Быстрая сортировка Среднее O(N log N), худший вариант O(N^2). Чтобы пренебречь ужасным вариантом
#нужно брать рандомный элемент (лучший вариант при отсортированном списке)

def partition(arr: List[int], low: int, high: int) -> int:

    rand_index = random.randint(low, high)
    arr[rand_index], arr[high] = arr[high], arr[rand_index]

    element = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= element:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr: List[int], low: int, high: int):
    if low < high:
        rand_index = partition(arr, low, high)

        quicksort(arr, low, rand_index - 1)
        quicksort(arr, rand_index + 1, high)


@time_it
def quicksort_wrapper(arr: List[int]) -> List[int]:
    arr_copy = arr[:]
    quicksort(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


