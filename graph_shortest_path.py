from collections import deque

edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v'],
]

def shortest_path(edges, node_a, node_b):
    graph = build_graph(edges)
    queue = deque([(node_a, 0)])
    # queue.append((node_a, 0))
    visited = set(node_a)

    while len(queue) > 0:
        node, distance = queue.popleft()

        if node == node_b:
            return distance
        
        for each in graph[node]:
            if each not in visited:
                visited.add(each)
                queue.append((each, distance + 1))
    return -1

def build_graph(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


print(shortest_path(edges, 'x', 'z'))