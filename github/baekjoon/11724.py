
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)

def dfs(v, visited):
    visited[v] = 1
    for temp in arr[v]:
        if visited[temp] != 1:
            dfs(temp,visited)
            
        

for i in range(m):
    u,v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
answer = 0
for k in range(1,n+1):
    if visited[k] == 0:
        dfs(k, visited)
        answer += 1
    
    
print(answer)
    

    

