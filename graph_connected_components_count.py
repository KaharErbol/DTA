graph = {
    3: [],
    4: [6],
    6: [4,5,7,8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1],
}

def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1
    
    return count

def explore(graph, curr, visited):
    if curr in visited:
        return False
    visited.add(curr)

    for each in graph[curr]:
        explore(graph, each, visited)

    return True


print(connected_components_count(graph))