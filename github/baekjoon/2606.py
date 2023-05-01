import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
visited = [0] * (n+1)
arr= [[] for _ in range(n+1)]


for i in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs(arr, v, visited):
    visited[v] = 1
    for i in arr[v]:
        if visited[i] == 0:
            bfs(arr, i, visited)


bfs(arr, 1, visited)
answer = 0

for j in range(2,len(visited)):
    if visited[j] == 1:
        answer += 1

print(answer)

    



