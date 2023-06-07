grid = [
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'w'],
    ['w', 'w', 'l', 'l', 'w'],
    ['l', 'w', 'w', 'l', 'l'],
    ['l', 'l', 'w', 'w', 'w'],
]

def island_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1
    return count


def explore(grid, r, c, visited):
    row_inbounds = 0 <= r and r < len(grid)
    col_inbounds = 0 <= c and c < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return False
    
    if grid[r][c] == 'w':
        return False
    
    position = (r,c)

    if position in visited:
        return False
    
    visited.add(position)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True



### Test
print(island_count(grid))