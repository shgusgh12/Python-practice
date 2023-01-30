from collections import deque
n, m, v = map(int, input().split())

graph = [[] for _ in range (n + 1)]

visited = [False] * (n + 1)
visited2 = [False] * (n + 1)
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1):
    graph[i].sort()

def dfs (graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs (graph, i, visited)
    

def bfs (graph, start, visited):
    queue = deque()
    queue.append(start)
    visited2[start] = True
    while queue:
        cnt = queue.popleft()
        print(cnt, end=' ')
        for i in graph[cnt]:
            if visited2[i] == False:
                queue.append(i)
                visited2[i] =True
            




dfs(graph,v,visited)
print()
bfs(graph,v,visited2)