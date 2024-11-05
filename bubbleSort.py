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
