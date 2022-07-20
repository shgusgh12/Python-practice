N = int(input())
arr = [0] * 10000

for i in range(N):
    a= int(input())
    arr[a-1] += 1    #index에 해당하는 숫자를 증가시킴

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)