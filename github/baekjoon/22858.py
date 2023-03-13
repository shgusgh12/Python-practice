import sys


n, k = map(int, sys.stdin.readline().split())

s = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))

for i in range(k):
    p = [0]*n
    for j in range(n):
        idx = d[j]
        p[idx - 1] = s[j]
    s = p

print(*s) # * 사용시 대괄호 삭제
    

        
