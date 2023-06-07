graph = {
    0: [8,1,5],
    1: [0],
    5: [0,8],
    8: [0,5],
    2: [3,4],
    3: [2,4],
    4: [3,2],
}

def largest_component(graph):
    largest = 0
    visited = set()
    for node in graph:
        size = explore_size(graph, node, visited)
        largest = max(largest, size)

    return largest

def explore_size(graph, node, visited):
    if node in visited:
        return 0
    
    visited.add(node)

    size = 1

    for each in graph[node]:
        size += explore_size(graph, each, visited)

    return size

print(largest_component(graph))
