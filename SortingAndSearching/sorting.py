def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        lowest_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[lowest_index]:
                lowest_index = j
        arr[i], arr[lowest_index] = arr[lowest_index], arr[i]
    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
    

    def quick_sort(arr, start, end):

        def quick_sort1(arr, start, end):
            if start < end:
                p_index = pivot(arr, start, end)
                quick_sort1(arr, start, p_index - 1)
                quick_sort1(arr, p_index + 1, end)

        def pivot(arr, start, end):
            pivot = arr[end]
            pivot_index = start
            for i in range(start, end):
                if arr[i] <= pivot:
                    arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                    pivot_index += 1
            arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
            return pivot_index
        quick_sort1(arr, start, end)
        return arr


a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
a = [3, 2, 4, 2, 1, 4, 2, 3, 78]
a = [10,9,8,7,6,5,4,3,2,1]
# print("Bubble Sort    : ", bubble_sort(a))
# print("Selection Sort : ", selection_sort(a))
# print("Insertion Sort : ", insertion_sort(a))
print("Merge Sort     : ", merge_sort(a))

