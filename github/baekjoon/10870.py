n = int(input())

arr=[0] * (21)

arr[1] = 1

for i in range(2,n+1):
    if arr[i] == 0:
        arr[i] = arr[i-2] + arr[i-1]


print(arr[n])

