import sys

input = sys.stdin.readline
N, M = map(int, input().split(' '))
arr =[False, False] + [True] * 999
cnt = []
for i in range(2, 1001):
    if arr[i] : 
        cnt.append(i)
        for j in range(2*i, 1001, i):
            arr[j] = False

for i in range(N, M+1):
    if arr[i] == True:
        print(i)
