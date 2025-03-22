#2.	Implement Selection sort 

# Selection Sort Implementation

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the minimum is at index i
        min_index = i
        
        # Find the index of the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
numbers = [64, 25, 12, 22, 11]
print("Original Array:", numbers)

selection_sort(numbers)
print("Sorted Array:", numbers)

