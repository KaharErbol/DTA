def how_sum(target, numbers):
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target+1):
        if table[i] is not None:
            for num in numbers:
                if (i+num) <= target:
                    table[i + num] = [*table[i], num]

    return table[target]

print(how_sum(7, [2,3]))

"""
0  1  2    3     4      5         6          7
[]   [2]  [3]  [2,2]   [3,2]    [2,2,2]     [3,2,2]
"""