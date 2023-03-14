import sys
# sys.stdin.readline().split()


#빈 배열을 이용하여 이전값을 저장후 현재값을 옮기는 방법

t = int(input())

def turn (n,d, arr):
    
    n-=1
    cnt = abs(d) // 45  #절댓값으로 해결
    minus = False
    if d< 0:
        minus = True
    
    for _ in range(cnt):
        if not minus:
            temp = list()
            for i in range(n + 1): #첫번째 대각선
                temp.append(arr[i][i])
            
            for i in range(n + 1): #메인 대각선 회전
                previous = arr[i][(n+1)//2]
                arr[i][(n+1)//2] = temp[i]
                temp[i] = previous

            for i in range(n+1):
                previous = arr[i][n-i]
                arr[i][n-i] = temp[i]
                temp[i] = previous
            
            for i in range(n+1):
                previous = arr[(n+1)//2][n -i]
                arr[(n+1)//2][n-i] = temp[i]
                temp[i] = previous
            
            for i in range(n+1):
                arr[n-i][n-i] = temp[i]
        else: #반시계 돌리기
            temp = list()
            for i in range(n + 1): #첫번째 대각선
                temp.append(arr[i][i])
            
            for i in range(n + 1): 
                previous = arr[(n+1)//2][i]
                arr[(n+1)//2][i] = temp[i]
                temp[i] = previous

            for i in range(n+1):
                previous = arr[n-i][i]
                arr[n-i][i] = temp[i]
                temp[i] = previous
            
            for i in range(n+1):
                previous = arr[n-i][(n+1)//2]
                arr[n-i][(n+1)//2] = temp[i]
                temp[i] = previous
            
            for i in range(n+1):
                arr[n-i][n-i] = temp[i]



            


for i in range(t):
    n, d = map(int,input().split())
    arr = [list(map(int,input().split(' '))) for _ in range(n)]
    turn(n,d,arr)


    for j in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()


    