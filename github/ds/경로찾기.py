from collections import defaultdict ,deque

n = int(input())
queue = deque()
matrix = [list(map(int,input().split())) for _ in range(n)]
answer = [[0 for _ in range(n)] for _ in range(n)]

def bfs(i):
    visited = [0 for _ in range(n)]
    queue.append(i)

    while queue:
        cur_v = queue.popleft()
        
        for k in range(n):
            # 방문안한 노드인데 cur_v => k가 경로가 있다면
            if visited[k] == 0 and matrix[cur_v][k] == 1:
                # 다음 K 탐색 그리고 K 방문 완료
                queue.append(k)
                visited[k] = 1
                answer[i][k] = 1

for i in range(n):
    bfs(i)
    
for i in answer:
    print(*i)



