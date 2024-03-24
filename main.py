import time
import random
import heapq


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr


def sort_with_algorithm(algorithm, arr):
    start_time = time.time()

    if algorithm == 'merge':
        sorted_arr = merge_sort(arr.copy())
    elif algorithm == 'quicksort':
        sorted_arr = quick_sort(arr.copy())
    elif algorithm == 'selection':
        sorted_arr = selection_sort(arr.copy())
    elif algorithm == 'bubble':
        sorted_arr = bubble_sort(arr.copy())
    elif algorithm == 'insertion':
        sorted_arr = insertion_sort(arr.copy())
    elif algorithm == 'heapsort':
        sorted_arr = heap_sort(arr.copy())
    else:
        print("Invalid sorting algorithm selected.")
        return

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Sorted array using {algorithm} sort: {sorted_arr}")
    print(f"Execution time: {execution_time:.6f} seconds")

    return sorted_arr


if __name__ == "__main__":
    while True:
        input_array = input("Enter the array to be sorted (comma-separated integers): ")
        try:
            input_array = list(map(int, input_array.split(',')))
            break  # Break out of the loop if the input is valid
        except ValueError:
            print("Invalid input! Please enter integers separated by commas.")

    while True:
        print("Input Array:", input_array)
        selected_algorithm = input(
            "Enter sorting algorithm (merge/quicksort/selection/bubble/insertion/heapsort): ").lower()
        if selected_algorithm not in ['merge', 'quicksort', 'selection', 'bubble', 'insertion', 'heapsort']:
            print("Invalid sorting algorithm! Please enter a valid sorting algorithm.")
        else:
            sorted_array = sort_with_algorithm(selected_algorithm, input_array)
            while True:
                another_sort = input("Do you want to sort again? (yes/no): ").lower()
                if another_sort == 'yes':
                    selected_algorithm = input(
                        "Enter sorting algorithm (merge/quicksort/selection/bubble/insertion/heapsort): ").lower()
                    if selected_algorithm not in ['merge', 'quicksort', 'selection', 'bubble', 'insertion', 'heapsort']:
                        print("Invalid sorting algorithm! Please enter a valid sorting algorithm.")
                    else:
                        sorted_array = sort_with_algorithm(selected_algorithm, input_array)
                elif another_sort == 'no':
                    exit()
                else:
                    print("Invalid input! Please enter 'yes' or 'no'.")
