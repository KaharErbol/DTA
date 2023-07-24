def selection_sort(n: list) -> list:
    for i in range(len(n)-1):
        min_val_idx = i
        for j in range(i+1, len(n)):
            if n[j] < n[min_val_idx]:
                min_val_idx = j
        if min_val_idx != i:
            n[i], n[min_val_idx] = n[min_val_idx], n[i] 

    

n = [2,3,1,4,8]
selection_sort(n)
print(n)

