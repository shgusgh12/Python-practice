n = int(input())
visited = [0] * (n+1)
tree = [[] for _ in range(n+1)] 
visited[1] = 1
for _ in range(n-1):
    x,y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

def dfs(v):
    for i in tree[v]:
        if not visited[i]:
            visited[i] = v
            dfs(tree, i,visited)

dfs(1)

for i in range(2,n+1):
    print(visited[i])