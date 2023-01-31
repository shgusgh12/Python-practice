from collections import deque
n = int(input())
idx =deque(list(map(int, input().split())))
arr =deque([i for i in range(1,n+1)])

while idx:
    start = idx[0]
    if start > 0:
        idx.popleft()
        idx.rotate(-start + 1)
        # 숫자가 음수면 시계반대방향 양수면 시계 
        # +1 한이유 pop했기때문
        print(arr.popleft(), end=' ')
        arr.rotate(-start+1)
    else:
        idx.popleft()
        idx.rotate(-start)
        #음수라서 양수로 바꿔주기위해 -
        print(arr.popleft(), end=' ')
        arr.rotate(-start)



    