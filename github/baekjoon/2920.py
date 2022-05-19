a = list(map(int,input().split() ))
x =0
j = 8
k = 0
for i in range(1,9):
    if a[i-1] ==i:
        x = 1
for i in range(1,9):
    for k in range(8,0,-1):
        if a[i-1] == k:
            x = 2
if x == 1:
    print('ascending')
elif x==2:
    print('decending')
else :
    print('mixed')
