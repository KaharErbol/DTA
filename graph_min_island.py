grid = [
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'w'],
    ['w', 'w', 'l', 'l', 'w'],
    ['l', 'w', 'w', 'l', 'l'],
    ['l', 'l', 'w', 'w', 'w'],
]


def min_island(grid):
    visited = set()
    min_size = float('inf')
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid, r, c, visited)
            if size > 0 and size < min_size:
                min_size = size

    return min_size


def explore_size(grid, r, c, visited):
    row_in_bounds = 0 <= r and r < len(grid)
    col_in_bounds = 0 <= c and c < len(grid[0])
    
    if not row_in_bounds or not col_in_bounds:
        return 0
    
    if grid[r][c] == 'w':
        return 0
    
    position = (r,c)

    if position in visited:
        return 0
    
    visited.add(position)

    size = 1

    size += explore_size(grid, r - 1, c, visited)
    size += explore_size(grid, r + 1, c, visited)
    size += explore_size(grid, r, c - 1, visited)
    size += explore_size(grid, r, c + 1, visited)

    return size


print(min_island(grid))
