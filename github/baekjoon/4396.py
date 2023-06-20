import sys
input = sys.stdin.readline

n = int(input())

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

ground = [list(input().rstrip()) for i in range(n)]
mine = [list(input().rstrip()) for j in range(n)]

over = False
tmp = []
for i in range(n):
    for j in range(n):
        if mine[i][j] == 'x' and ground[i][j] =='*':
            over =True
        if mine[i][j] == 'x':
            cnt = 0
            for k in range(8):
                if n > i+dx[k] >= 0 and 0 <= j+dy[k]< n and ground[i+dx[k]][j+dy[k]] =='*':
                    cnt +=1
            mine[i][j] = str(cnt)

if over:
    for i in range(n):
        for j in range(n):
            if ground[i][j] == '*':
                mine[i][j] = '*'

for a in mine:
    print(''.join(a))



                            



