from collections import deque
N, M = map(int, input().split(' '))

q = deque()
arr = [0] * N
for i in range(1,N+1):
    q.append(i)
num = 0
while len(q):
    for i in range(M-1):
        q.append(q[0])
        q.popleft()
    arr[num] = q[0]
    num += 1
    q.popleft()
k = 0
print('<', end='')
for i in range(N):
    print(arr[i],end='')
    if i != (N-1):
        print(",",end=' ')
print('>')