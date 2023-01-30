from collections import deque
n,m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
#동서남북 좌표
answer = 0
#시작좌표 1,1
def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            x = x +dx[i]
            y = y +dy[i]
            if x < 0 or y < 0 or x > n or y > m:
                continue
            queue.append([x,y])
    return True

for i in range(n):
    for j in range(m):
        if bfs(i,j) != True:
            answer +=1
print(answer)

    
            

bfs(1,1)


