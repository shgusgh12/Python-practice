a = list(map(int, input().split()))
for i in range(1,8):
    if a[i-1] == i:
        x = 1
    else:
        x = 0
        break
i = 0
if x != 1: 
    for j in range(8,1,-1):
        if a[i] == j:
            i = i+1
            x = 2
        else:
            x = 0
            break
        

if x == 1:
    print('ascending')
elif x==2:
    print('decending') 
else:
    print('mixed')    
    