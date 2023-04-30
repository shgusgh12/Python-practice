import sys

input = sys.stdin.readline

dp = [0]
n = int(input())
arr = list(map(int, input().split()))
m = int(input())

temp = 0
for i in arr:
    temp += i
    dp.append(temp)


for k in range(m):
    i, j = map(int, input().split())
    print(dp[j]-dp[i-1])

