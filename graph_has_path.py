from collections import deque

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

def has_path_dfs(graph, src, dst):
    if src == dst:
        return True
    
    for each in graph[src]:
        if has_path_dfs(graph, each, dst):
            return True
    
    return False


print("DFS: ",has_path_dfs(graph, 'f', 'j'))


def has_path_bfs(graph, src, dst):
    queue = deque()
    queue.append(src)

    while len(queue) > 0:
        curr = queue.popleft()
        if curr == dst:
            return True
        
        for each in graph[curr]:
            queue.append(each)

    return False

print("BFS: ", has_path_bfs(graph, 'f', 'k'))