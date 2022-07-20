from re import L


M = int(input())
tmp = list(input())
d = '0abcdefghijklmnopqrstuvwxyz'
num = 0
cnt =0 
for i in range(M):
    for j in range(27):
        if tmp[i] == d[j]:
            cnt += 31**(num) * j
            num += 1
print(cnt)

