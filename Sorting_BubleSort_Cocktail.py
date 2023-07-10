def bubble_sort(arr):
    while True:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        
        for j in range(len(arr) - 1, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True

        if not swapped:
            break
    
    return arr

arr = [211, 3, 5, 6, 1, 2, 33, 1, 1]

print(bubble_sort(arr))

# Complexity
# Time: O(N^2)
# SPACE: O(1)