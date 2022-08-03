#블록 넣으면 2초 블록 꺼내서 놓으면 1초 블록은 1
import sys
input = sys.stdin.readline 
N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 10000000000
height = 0
for k in range(257):
    max = 0
    min = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= k:
                max += arr[i][j] - k
            else:
                min += k - arr[i][j]
    if max + B < min:
        continue
    T = max * 2 + min
    if T <= ans:
        ans = T
        height = k
print(ans , height)