import sys
input = sys.stdin.readline
n = int(input())
arr = [0]+list(map(int, input().split()))
stu = int(input())
def change(x):
    global arr
    arr[x] = abs(arr[x]-1)
for i in range(stu):
    gender, data = map(int, input().split())
    if gender == 1:
        for i in range(data,n+1, data):
            change(i) 
    else:
        change(data)
        for j in range(n//2):
            if data - j < 1 or data + j > n:
                break
            if arr[data + j] == arr[data-j]:
                change(data + j)
                change(data - j)
            else:
                break

for i in range(1, n+1):
    print(arr[i], end=' ')
    if i%20 == 0:
        print()
    
    