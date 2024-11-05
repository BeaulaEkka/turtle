# iterate through a collection one element at a time
# runtime complexity:O(n)
# disadvantages:slow for large data sets
# Advantages:
# Fast for searches of small to medium data sets
# doesnt need to be sorted
# useful for data sturctures that do not have random access(linked List)

# Renamed 'list' to 'lst' to avoid overwriting the built-in 'list' keyword
def linear_search(lst, n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            print(f'found at index: {i}')
            return True
        i += 1  # Increment i to check the next element
    return False  # Only return False if no match is found after checking the whole list


# Example usage
lst = [5, 8, 9, 2]
n = 9
linear_search(lst, n)  # Should print 'found at index: 2'
