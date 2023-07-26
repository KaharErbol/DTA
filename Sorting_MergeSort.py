# Recursive, Divide and Conquer, Comparison-based

def merge_sort(n: list) -> list:
    if len(n) > 1:
        half = len(n) // 2

        # divide
        left = n[:half]
        right = n[half:]

        # recursion
        merge_sort(left)
        merge_sort(right)

        # merge
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                n[k] = left[i]
                i += 1
            else:
                n[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            n[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            n[k] = right[j]
            j += 1
            k += 1

n = [2,3,1,23,4,11,2,8,0]
merge_sort(n)
print(n)
