from isEven import isEven_upgrade, isEven
from queues import Queue_List, Queue_Linked
from sort_algo import generate_random_array, merge_sort_wrapper, timsort_wrapper, quicksort_wrapper


def first_task(value: int):
    print("---Запуск первой задачи---")
    result_simple = isEven(value)
    print(f"Результат isEven: {result_simple}")

    result_robust = isEven_upgrade(value)
    print(f"Результат isEven_upgrade: {result_robust}")
    print("=============================")

    return result_simple, result_robust


def second_task():
    print("---Запуск второй задачи---")
    print("Тест: Queue_List")
    q_list = Queue_List()
    q_list.insert(10)
    q_list.insert(20)
    q_list.insert(414)
    print(q_list)

    print(f"Удаленный элемент: {q_list.remove()}")
    print(q_list)

    print("Тест: Queue_Linked")
    q_linked = Queue_Linked()
    q_linked.insert(431)
    q_linked.insert("A")
    q_linked.insert(1443)
    print(q_linked)
    print(f"Удаленный элемент: {q_linked.remove()}")
    print(q_linked)
    print("=============================")


def third_task(size: int):
    # Генерация случайного (неотсортированного) массива
    print(f"---Запуск третьей задачи: Сортировка массива с размером N={size} ---")
    original_array = generate_random_array(size)
    print(f"Массив на тест: {original_array[:10]}...")

    # -----------------------------------------------------------
    # 1. Тест Merge Sort на СЛУЧАЙНОМ массиве
    # -----------------------------------------------------------
    print("\nТестирование сортировки слиянием, стабильно O(N Log N)")
    copy_for_merge = original_array[:]
    sorted_result_random = merge_sort_wrapper(copy_for_merge)
    print(f"Отсортированный массив часть: {sorted_result_random[:10]}...")

    # -----------------------------------------------------------
    # 2. Тест Timsort на СЛУЧАЙНОМ массиве
    # -----------------------------------------------------------
    print("\nТестирование встроенной сортировки (Timsort)")
    copy_for_timsort = original_array[:]
    sorted_result_random_timsort = timsort_wrapper(copy_for_timsort)
    print(f"Отсортированный массив Timsort (часть): {sorted_result_random_timsort[:10]}...")

    # -----------------------------------------------------------
    # 3. Тест Quick Sort на СЛУЧАЙНОМ массиве
    # -----------------------------------------------------------
    print("\nТестирование быстрой сортировки (Quick Sort), O(N Log N) в среднем")
    copy_for_quicksort = original_array[:]
    sorted_result_random_quick = quicksort_wrapper(copy_for_quicksort)
    print(f"Отсортированный массив QuickSort (часть): {sorted_result_random_quick[:10]}...")

    # -----------------------------------------------------------
    # Тест на УЖЕ ОТСОРТИРОВАННОМ массиве (для всех)
    # -----------------------------------------------------------
    print("\nТестирование на отсортированном массиве")
    fully_sorted_base = original_array[:]
    fully_sorted_base.sort()

    # Merge Sort на отсортированном
    copy_for_merge_sorted = fully_sorted_base[:]
    sorted_result_sorted_merge = merge_sort_wrapper(copy_for_merge_sorted)
    print(f"Merge Sort (сортированный) (часть): {sorted_result_sorted_merge[:10]}...")

    # Timsort на отсортированном
    copy_for_timsort_sorted = fully_sorted_base[:]
    sorted_result_sorted_timsort = timsort_wrapper(copy_for_timsort_sorted)
    print(f"Timsort (сортированный) (часть): {sorted_result_sorted_timsort[:10]}...")

    # Quick Sort на отсортированном
    copy_for_quicksort_sorted = fully_sorted_base[:]
    sorted_result_sorted_quick = quicksort_wrapper(copy_for_quicksort_sorted)
    print(f"Quick Sort (сортированный) (часть): {sorted_result_sorted_quick[:10]}...")

    print("=============================")


def main():
    first_task(144)
    second_task()
    size_third_task = 100000
    third_task(size_third_task)


if __name__ == "__main__":
    main()
