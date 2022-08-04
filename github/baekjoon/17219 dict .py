N, M = map(int, input().split())
arr ={}
for i in range(N):
    key, value = input().split()
    arr[key] = value     
#딕셔너리 입력시 split으로 나누어 입력
for i in range(M):
    print(arr[input().rstrip()])
#딕셔너리의 key값으로 list형이올수 없다