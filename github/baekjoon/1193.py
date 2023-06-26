x = int(input())

arr = [[0 for _ in range(x)] for _ in range(x)]

for i in range(10):
    for j in range(10):
        arr[i][j] = str(i) + '/' + str(j)

for i in arr:
    print(i)
    print()
