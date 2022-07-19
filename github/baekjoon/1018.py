#다시 풀기

N, M = map(int, input().split())
arr = []
count = []

for _ in range(N):
    arr.append(input())

for a in range(N-7):
    for b in range(M-7):
        idw = 0
        idb = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] != 'W':
                        idw += 1
                    if arr[i][j] != 'B':
                        idb += 1
                else:
                    if arr[i][j] != 'B':
                        idw+=1
                    if arr[i][j] != 'W':
                        idb+=1
        count.append(min(idw, idb))
print(min(count))