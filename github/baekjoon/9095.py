t = int(input())





for _ in range(t):
    num = int(input())
    
    
    dp = [0] * (11)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4,num+1):
        answer = 0
        for j in range(1,4):
            answer += dp[i-j]
        dp[i] = answer

    print(dp[num])  



