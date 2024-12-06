



def recur(idx, weight):
    global answer

    if weight > b:
        return -99999
    if idx == n:
        return 0
    
    if dp[idx][weight] != -1:
        return dp[idx][weight]
    
    dp[idx][weight] = max((recur(idx+1, weight+items[idx][0]) + items[idx][1]), recur(idx+1, weight))

    return dp[idx][weight]

n, b = map(int, input().split())

items = [list(map(int, input().split()))  for i in range(n)]

dp = [[-1 for _ in range(100001)] for _ in range(n)]

answer = 0



print(recur(0,0))