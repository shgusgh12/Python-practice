n,m = map(int, input().split())
#가로 m 세로 n
a,b,d = map(int, input().split())
result = 0
ground = [[0] * m for _ in range(n)]
ground[a][b] = 1
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            ground[i][j] = 1


watcha = 0
watchb = 0
nx = [0, -1, 0, 1]
ny = [-1, 0, 1, 0]
while True:
    nowx = a + nx[d]
    nowy = b + ny[d]

    if arr[nowx][nowy] == 0:
        ground[nowx][nowy] = 1
        a = nowx
        b = nowy
        d = d - 1
        result += 1
    else:
        d = d - 1

    if d == -4:
        d = -1

    if result == 3:
        break

print(result)