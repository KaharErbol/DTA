def canFinish(numCourses, prerequisites):
    graph = {}

    for i in range(numCourses):
        graph[i] = []

    for crs, pre in prerequisites:
        graph[crs].append(pre)

    visited = set()

    def dfs(crs):
        if crs in visited:
            return False
        if graph[crs] == []:
            return True
        
        visited.add(crs)
        for each in graph[crs]:
            if not dfs(each): return False

        visited.remove(crs)
        graph[crs] = []
        return True
    
    for crs in range(numCourses):
        if not dfs(crs): return False
    
    return True