from collections import deque

n, m = map(int, input().split())
#n 기차의 수 m 명령의 수

answer = 0
# 1 i x  
# i번째 기차에 x번 좌석에 태워라

train = [[False for _ in range(20)] for _ in range(n)]


for i in range(m):
    order = list(map(int, input().split()))
    tnum = order[1] - 1
    
    if order[0] == 1:
        sit = order[2] - 1
        train[tnum][sit] = True
    elif order[0] == 2:
        sit = order[2] - 1
        train[tnum][sit] = False
    elif order[0] == 3:
        train[tnum].insert(0, False)
        train[tnum].pop()
    else:
        train[tnum].pop(0)
        train[tnum].append(False)
            

tmp = []
for i in train:
    if i not in tmp:
        tmp.append(i)
    

print(len(tmp))
            


                
                




