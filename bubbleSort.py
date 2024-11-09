# bubble Sort
# time complexity-O(n^2)


def bubble_sort(arr):
    n = len(arr)
    flag = True  # No import needed; this is a simple boolean variable
    while flag:  # Loop until no swaps occur
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr


A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
sorted_array = bubble_sort(A)  # Sort the array
print("Sorted Array:", sorted_array)  # Print the sorted result
# Optimized
# The optimized version of bubble sort will have a more efficient big O runtime than the unoptimized version of bubble sort.
# Code


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort_unoptimized(arr):
    for el in arr:
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)


def bubble_sort_optimized(arr):
    for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]


# insertion Sort-O(n^2)
# space-O(1)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break


# selection Sort// sorted and unsorted part of the spray
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        print('i:', arr[i])
        for j in range(i+1, n):
            print('j:  ', arr[i+1])
            if arr[j] < arr[min_index]:
                print(f'swap with {arr[min_index]}')
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# merge Sort also called divide and conquer !
def merge_sort(items):
    if len(items) <= 1:
        return items

    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []

    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result


unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19,
                   202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(f'ordered_list1:{ordered_list1}')
print(f'ordered_list2:{ordered_list2}')
print(f'ordered_list3:{ordered_list3}')


# Example array
A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

# Copy the array for both sorting methods
A_unoptimized = A.copy()
A_optimized = A.copy()
A_insertion = A.copy()
A_selection = A.copy()


# Sort using the unoptimized bubble sort
bubble_sort_unoptimized(A_unoptimized)
print("Unoptimized Sorted Array:", A_unoptimized)

# Sort using the optimized bubble sort
bubble_sort_optimized(A_optimized)
print("Optimized Sorted Array:", A_optimized)

insertion_sort(A_insertion)
print('A_insertion', A_insertion)

selection_sort(A_selection)
print('selection_sort', A_selection)
print(merge([1, 8, 9, 25], [4, 6, 8, 9]))
