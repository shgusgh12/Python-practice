from collections import deque
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

def bfs (graph , start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

bfs(graph, 1 ,visited)
    

        
    