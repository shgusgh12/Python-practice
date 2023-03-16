import sys
from collections import deque
t = int(sys.stdin.readline())

# r 뒤집기 d는 버리기

for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = input()
    temp = []
    for i in range(len(arr)):
        if arr[i].isdigit():
            temp.append(arr[i])
    


    for j in range(len(p)):
        if temp:
            if p[j] == 'R':
                temp = temp[::-1]
            else:
                cnt =deque(temp)
                cnt.popleft()
                temp = list(cnt)

        else:
            print('error')
    print(temp)


    

