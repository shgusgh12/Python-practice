n, m = map(int, input().split())

s = []
arr = []
answer = 0
for i in range(n):
    s.append(input())

for i in range(m):
    arr.append(input())

for j in range(m):
    if arr[j] in s:
        answer += 1

print(answer)
            

