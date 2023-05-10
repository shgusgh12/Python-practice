import sys
input = sys.stdin.readline

n = int(input())
arr =[list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
#dp에 방문한 횟수를 저장함
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] != 0 and dp[i][j] !=0:
            #현재 위치에 이전 방문했던 위치의 방문 횟수를 더해줌
            if i + arr[i][j] < n:
                dp[i + arr[i][j]][j] += dp[i][j]
            if j + arr[i][j] < n:
                dp[i][j + arr[i][j]] += dp[i][j]
print(dp[-1][-1])

      