n = int(input())

arr = [0] * (n+1)
#arr에는 index가 1이 되기 위한 횟수의 최솟값이 들어간다

for i in range(2, n+1):
    arr[i] = arr[i-1] + 1
    # arr[i-1]에서 하나만 더 연산하면 arr[i] 가 될수 있기 때문에 1을 더해준다
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2]+1)

    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3] + 1)

    
print(arr[n])
 