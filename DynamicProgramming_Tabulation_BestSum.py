def best_sum(target, numbers):
    table = [-1] * (target + 1)
    table[0] = []
    for i in range(target+1):
        if table[i] != -1:
            for num in numbers:
                combo = [*table[i], num]
                if (i + num) <= target:
                    if table[i + num] == -1 or len(combo) < len(table[i + num]):
                        table[i + num]  = combo

    return table[target]

print(best_sum(7, [5,3,4,7]))
print(best_sum(11, [1,2,5]))
print(best_sum(3, [2]))
print(best_sum(100, [2,3,25]))