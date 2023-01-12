n = int(input())
move = input().split()
x = 1
y = 1
#벡터
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
#동 북 서 남
for i in move:
    if i == 'R':
        nx = x + dx[0]
        ny = y + dy[0]
    elif i == 'D':
        nx = x + dx[3]
        ny = y + dy[3]
    elif i == 'U':
        nx = x + dx[1]
        ny = y + dy[1]
    elif i == 'L':
        nx = x + dx[2]
        ny = y + dy[2]
    #행렬 범위 넘을 경우 제외
    if ny > n or nx > n or ny < 1 or nx < 1:
        continue
    #범위 내에 존재한다면 값 누적
    x, y = nx, ny
print(nx,ny)      

# if else문 대신 for문으로 간단하게 
# move_type = ['R','U','L','D']
# for i in move:
#     for j in range(len(move_type)):
#         if i == move_type[j]:
#             nx = x + dx[j]
#             ny = y + dy[j]
#     if ny > n or nx > n or ny < 1 or nx < 1:
#         continue
#     x, y = nx, ny
# print(x,y)    
