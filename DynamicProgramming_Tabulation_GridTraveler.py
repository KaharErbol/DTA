def grid_traveler_tabulation(m, n):
    table = [[0] * (n + 1) for _ in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            curr = table[i][j]
            if (i+1) <= m:
                table[i+1][j] += curr
            if (j+1) <= n:
                table[i][j+1] += curr
    return table[m][n]


print(grid_traveler_tabulation(3,2))
print(grid_traveler_tabulation(18,18))