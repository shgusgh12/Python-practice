n = int(input())
arr=[]
for i in range(n):
    [x,y] = map(int, input().split())
    arr.append([x,y])

arr2 = sorted(arr)

for i in range(n):
    print(arr2[i][0], arr2[i][1])