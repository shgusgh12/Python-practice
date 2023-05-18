import sys
from collections import deque
input = sys.stdin.readline
arr = deque()
n, m = map(int, input().split())

for i in range(1,n+1):
    arr.append(i)
delete = list(map(int, input().split()))

answer = 0
for j in delete:
    first = arr[0]
    if first == j:
        arr.popleft()
    while j != first:
        mid = len(arr)//2
        idx = arr.index(j)
        if idx > mid:
            arr.rotate(1)
            answer += 1
            first = arr[0]
            if first == j:
                arr.popleft()
        else:
            arr.rotate(-1)
            answer += 1
            first = arr[0]
            if first == j:
                arr.popleft()

    
print(answer)



    
