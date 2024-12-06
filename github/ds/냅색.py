import sys
input = sys.stdin.readline

n, k= map(int, input().split())

items = [list(map(int, input().split())) for _ in range(n)]

dp= [[-1 for _ in range(100_001)] for _ in range(n)]



def recur(idx, w, v):
    

    if idx == n:
        return
    if w > k:
        return
  
        

    recur(idx + 1, list[idx][0] + w, list[idx][1] + v)
    recur(idx +1 , w, v)


recur(0, 0, 0)
print(answer)