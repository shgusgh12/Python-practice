n,m = map(int, input().split())
a,b,d = map(int, input().split())
# 체크한 땅 표시
ground = [[0] * m for _ in range(n)]
ground[a][b] = 1 
arr = []
#입력받은 땅 구조
for i in range(n):
    arr.append(list(map(int, input().split())))


nx = [-1, 0, 1, 0]
ny = [0, 1, 0, -1]


def left():
    #d가 함수 바깥에서 사용된 전역변수 이기 때문에 
    #함수 안에서 사용 할 경우 global을 붙여 줘야 한다
    global d
    d -= 1
    if d == -1:
        d = 3
    
result =1  #처음 시작점에서 이미 하나 체크
turn_time = 0 #회전한 횟수 while 탈출위해 필요
while True:
    left() #먼저 왼쪽으로 회전
    nowx = a + nx[d]
    nowy = b + ny[d]

    if arr[nowx][nowy] == 0 and ground[nowx][nowy] == 0: #이동한경우
        ground[nowx][nowy] = 1
        a = nowx
        b = nowy
        result += 1
        turn_time = 0
        continue
    else:
        turn_time += 1 #막혀있어서 왼쪽으로 회전

    if turn_time == 4:
        nowx = a - nx[d]
        nowy = b - ny[d]
        if arr[nowx][nowy] == 0:
            a = nowx
            b = nowy
        else:
            break
        turn_time = 0
        

print(result)