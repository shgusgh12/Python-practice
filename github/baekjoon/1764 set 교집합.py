#교집합 set을 사용해 시간을 줄여야함
N, M = map(int, input().split())
arr = set()
arr2 = set()
ans = 0 
for i in range(N):
    arr.add(input())
for j in range(M):
    arr2.add(input())
arr3 = sorted(list(arr & arr2))
print(len(arr3))
for i in range(len(arr3)):
    print(arr3[i])