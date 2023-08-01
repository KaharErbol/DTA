def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1 


def quick_sort(arr, low, high):
    if low < high:
        pv = partition(arr, low, high)

        quick_sort(arr, low, pv - 1)

        quick_sort(arr, pv + 1, high)

arr = [3,1,7,2,11,2,10,9]

quick_sort(arr,0, len(arr) - 1)
print(arr)