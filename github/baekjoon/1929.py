import sys
input = sys.stdin.readline
N, M = map(int, input().split(' '))
arr =[]
for i in range(M+1):
    arr[i] = i

for i in range(2, M+1):
    for j in range(2*i,M+1):
        if arr[i*j] != 0:
            arr[i*j] = 0 


