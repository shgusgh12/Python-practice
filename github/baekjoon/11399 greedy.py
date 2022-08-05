N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
ans = 0
j = 0
for k in range(N, 0, -1):
    ans += arr[j] * k
    j += 1
print(ans)
    