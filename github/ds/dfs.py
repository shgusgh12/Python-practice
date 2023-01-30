# 인접 matrix
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
def dfs (visited, v, graph):
    visited[v] = True
    print(v , end=' ')

    for i in graph[v]:
        if visited[i] == False:
            dfs(visited, i, graph)

dfs(visited, 1, graph)
    
    

        
    