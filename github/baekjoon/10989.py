N = int(input())
arr = []
for i in range(N):
     arr.append(int(input()))
arr2 = sorted(arr)
for i in range(N):
    print(arr2[i])