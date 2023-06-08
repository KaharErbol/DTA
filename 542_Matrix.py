from collections import deque

def update_matrix(mat):
    queue = deque()
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                queue.append((r,c))
            else:
                mat[r][c] = '*'
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            row = r + dr
            col = c + dc
            row_inbounds = 0 <= row < len(mat)
            col_inbounds = 0 <= col < len(mat[0])
            if row_inbounds and col_inbounds and mat[row][col] == '*':
                mat[row][col] = mat[r][c] + 1
                queue.append((row, col))
                
    return mat


mat = [
    [0,0,0],
    [0,1,0],
    [1,1,1],
]

print(update_matrix(mat))
