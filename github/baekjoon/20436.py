
import sys
input = sys.stdin.readline

left, right = input().rstrip().split()
ans = input().rstrip()

a = ['qwertyuiop','asdfghjkl','zxcvbnm']
no = 'yuiophjklbnm'
res = 0
lx = 0
ly = 0
rx = 0
ry = 0
for i in range(len(a)):
    if left in a[i]:
        lx = i 
        ly = a[i].index(left)
    if right in a[i]:
        rx = i
        ry = a[i].index(right)

for k in ans:
    res += 1
    if k in no:
        for i in range(len(a)):
            if k in a[i]:
                sx = i
                sy = a[i].index(k)
                res += abs(sx-rx) + abs(sy-ry)
                rx = sx
                ry = sy
                break
    else:
        for i in range(len(a)):
            if k in a[i]:
                sx = i
                sy = a[i].index(k)
                res += abs(sx-lx) + abs(sy-ly)
                lx = sx
                ly = sy
                break
        

print(res)
    
