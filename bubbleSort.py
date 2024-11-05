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
## Optimized 
#The optimized version of bubble sort will have a more efficient big O runtime than the unoptimized version of bubble sort.
#Code


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


#insertion Sort-O(n^2)
#space-O(1)


# Example array
A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

# Copy the array for both sorting methods
A_unoptimized = A.copy()
A_optimized = A.copy()

# Sort using the unoptimized bubble sort
bubble_sort_unoptimized(A_unoptimized)
print("Unoptimized Sorted Array:", A_unoptimized)

# Sort using the optimized bubble sort
bubble_sort_optimized(A_optimized)
print("Optimized Sorted Array:", A_optimized)
