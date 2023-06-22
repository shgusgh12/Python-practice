import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
answer = []
for _ in range(5):
    answer += list(map(int, input().split()))


def check():
    bingo = 0
    for row in arr:
        if row.count(0) == 5:
            bingo += 1
    
    for i in range(5):
        cnt = 0
        for ja in range(5):
            if arr[ja][i] == 0:
                cnt += 1
        if cnt == 5:
            bingo += 1
    tmp = 0
    for j in range(5):
        if arr[j][j] == 0:
            tmp += 1
    if tmp == 5:
        bingo += 1
    ctmp = 0
    for j in range(5):
        if arr[j][4-j] == 0:
            ctmp += 1
    if ctmp ==5:
        bingo += 1
    
    return bingo
            

count = 0
for k in range(25):
    for i in range(5):
        for j in range(5):  
            if answer[k] == arr[i][j]:
                arr[i][j] = 0
                count +=1
    if count >= 12:
        res = check()
        if res >= 3:
            print(k+1)
            break
                
                
                    


