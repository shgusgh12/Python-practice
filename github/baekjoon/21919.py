import sys
n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
l = max(arr)
prime = [0] * (l+1)
#0이 소수
for i in range(2,l+1):
    if prime[i] == 1:
        continue
    for j in range(2*i, l+1, +i):
        prime[j] = 1
answer = 1
arr2 = set(arr)
arr = list(arr2)
for i in range(len(arr)):
    if prime[arr[i]] == 0:
        answer *= arr[i]

if answer == 1:
    print(-1)
else:
    print(answer)



