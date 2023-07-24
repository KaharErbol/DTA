def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

items = [211, 3, 5, 6, 1, 2, 33, 1, 1]
# i = 0        2, 3, 4, 1, 2, 6, 1, 1, 33
# i = 1        2, 3, 1, 2, 4, 1, 1, 6, #33
# i = 2        2, 1, 2, 3, 1, 1, 4, #6, 33
# i = 3        1, 2, 2, 1, 1, 3, #4, 6, 33
# i = 3        1, 2, 1, 1, 2, #3, 4, 6, 33
# ... 
print(bubble_sort(items))

# Complexity
# Time: O(N^2)
# Space: O(N)