def insertion_sort(n: list) -> list:
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1

        while j >= 0 and key < n[j]:
            n[j + 1] = n[j]
            j -= 1
        
        n[j + 1] = key
    

n = [ 40, 13, 20, 8]
insertion_sort(n)
print(n)
