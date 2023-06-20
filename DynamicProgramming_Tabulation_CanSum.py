def can_sum_tabulation(target, numbers):
    table = [False] * (target + 1)
    table[0] = True

    for i in range(target + 1):
        if table[i]:
            for num in numbers:
                if (i+num) <= target:
                    table[i+num] = True
    return table[target]

print(can_sum_tabulation(7, [5, 3, 4, 7]))