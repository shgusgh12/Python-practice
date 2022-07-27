N, M, B = map(int, input().split(' '))
arr = []
arr2 = []
for i in range(N):
    arr2 = map(int, input().split(' '))
    arr.append([arr2])
print(arr)