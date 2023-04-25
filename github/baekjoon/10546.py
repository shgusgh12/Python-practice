import sys

n = int(input())
arr= {}
for i in range(n):
    k = input()
    if k in arr:
        arr[k] += 1
    else:
        arr[k] = 1

for _ in range(n-1):
    k = input()
    if k in arr : 
        arr[k] -= 1
    if arr[k] == 0:
        del arr[k]


for k in arr.keys():
    print(k)