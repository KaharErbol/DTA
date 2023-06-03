graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

def dfs_iterate(graph, source):
    stack = [source]

    while len(stack) > 0:
        curr = stack.pop()
        print(curr)

        for each in graph[curr]:
            stack.append(each)


def dfs_recursive(graph, source):
    print(source)

    for each in graph[source]:
        dfs_recursive(graph, each)

print("Iterative approach: ")
print(dfs_iterate(graph, 'a'))

print("Recursive approach: ")
print(dfs_recursive(graph, 'a'))