n,m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
answer = []

def recur(curr):
    if len(curr) == m:
        answer.append(curr)
        return
    
    for i in range(n):
        if len(curr) != 0 and curr[-1] <= nums[i]:
            curr.append(nums[i])
        elif len(curr) == 0:
            curr.append(nums[i])
        else:
            continue
        recur(curr[:])
        curr.pop()
    
recur([])

for a in answer:
    print(*a)
