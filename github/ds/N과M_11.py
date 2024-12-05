import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 1 2 

nums = list(map(int, input().split()))
nums.sort()
new = list(set(nums))
new.sort()


answer = []
def recur(curr):
    if len(curr) == m:
        answer.append(curr)
        return
    
    for i in range(len(new)):
        curr.append(new[i])
        recur(curr[:])
        curr.pop()

recur([])

for a in answer:
    print(*a)

