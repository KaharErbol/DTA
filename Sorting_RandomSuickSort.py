import random

def partition_rand(arr, start, end):
    rand_pv = random.randrange(start, end)

    arr[start], arr[rand_pv] = arr[rand_pv], arr[start]

    return partition(arr, start, end)


def partition(arr, start, end):
    pv = start
    i = start + 1

    for j in range(start + 1, end + 1):
        if arr[j] <= arr[pv]:
            arr[j], arr[i] = arr[j], arr[i]
            i += 1
    arr[pv], arr[i-1] = arr[i-1], arr[pv]

    pv = i - 1
    return pv

def rand_quicksort(arr, start, end):
    if start < end:
        pv = partition_rand(arr, start, end)
        rand_quicksort(arr, start, pv - 1)
        rand_quicksort(arr, pv + 1, end)

arr = [3,1,7,2,11,2,10,9]
rand_quicksort(arr, 0, len(arr)-1)
print(arr)