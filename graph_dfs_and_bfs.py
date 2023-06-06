from collections import deque

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

# print("DFS Iterative approach: ")
# print(dfs_iterate(graph, 'a'))

# print("DFS Recursive approach: ")
# print(dfs_recursive(graph, 'a'))


# Depth First Search
def bfs_iterative(graph, source):
    queue = deque()
    queue.append(source)

    while len(queue) > 0:
        curr = queue.popleft()
        print(curr)
        for each in graph[curr]:
            queue.append(each)


print("BFS Iterative Approach:")
print(bfs_iterative(graph, 'a'))
