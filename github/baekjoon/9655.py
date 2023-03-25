n = int(input())

#상근 창영 상근 창영

dp = [0] * (n+1)


for i in range(1, n+1):
    if i % 2 == 0:
        dp[i] = 'CY'
    else:
        dp[i] = 'SK'

print(dp[n])


