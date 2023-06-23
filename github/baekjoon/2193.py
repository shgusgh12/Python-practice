import sys
input = sys.stdin.readline

n = int(input())

dp = [0,1,1,2,3]
for i in range(4,n+1):
    dp.append(dp[i] + dp[i-1])

print(dp[n])


