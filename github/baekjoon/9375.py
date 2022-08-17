from collections import Counter
t = int(input())

for i in range(t):
    arr = []
    
    j = int(input())
    for k in range(j):
        key, type = input().split()
        arr.append(type)
    c = Counter(arr)
    cnt = 1
    if len(c) == 1:
        print(c[type])
    else:
        for i in c:
            cnt*=c[i]+1
        print(cnt-1)
        


    
              