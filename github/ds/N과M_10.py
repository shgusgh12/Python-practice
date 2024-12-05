import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

# 1 7 9 9 
answer = []
def recur(curr, start):
    if len(curr) == m:
        if curr in answer:
            return
        answer.append(curr)
        return
    
    for i in range(start, n):
        curr.append(nums[i])
        recur(curr[:], i+1)
        curr.pop()


recur([], 0)

for a in answer:
    print(*a)