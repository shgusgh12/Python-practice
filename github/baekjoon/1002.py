import math
t = int(input())


for i in range(t):  
    x,y,r,x2,y2,r2 = map(int, input().split())
    cnt = math.sqrt((x-x2)**2 + (y-y2)**2)
    if cnt == 0 and r == r2:
        print(-1)
    elif cnt == r+r2 or abs(r-r2) == cnt:
        print(1)
    elif abs(r-r2) < cnt < r+r2:
        print(2)
    else:
        print(0)