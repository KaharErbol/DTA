# edges list
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]

# adjacency list
# graph = {
#     'i': ['j', 'k'],
#     'j': ['i'],
#     'k': ['i', 'm', 'l', 'j'],
#     'm': ['k'],
#     'l': ['k'],
#     'o': ['n'],
#     'n': ['o'],
# }

def undirected_path(edges, node_a, node_b):
    graph = build_graph(edges)
    s = set()
    return has_path(graph, node_a, node_b, s)

def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    
    for each in graph[src]:
        if has_path(graph, each, dst, visited):
            return True

    return False    

def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

print("undirected path: ", undirected_path(edges, 'j', 'o'))