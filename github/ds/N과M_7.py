
n,m = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

answer = []
def recur(curr):
    if len(curr) == m:
        answer.append(curr)
        return
    
    for i in range(n):
        curr.append(nums[i])
        recur(curr[:])
        curr.pop()

recur([])

for a in answer:
    print(*a)
    