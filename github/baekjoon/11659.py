n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0]
temp = 0
for sum in arr:
    temp += sum
    dp.append(temp)
for k in range(m):
    i, j = map(int, input().split())
    print(dp[j]-dp[i])



