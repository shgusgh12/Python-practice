
n,m = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

# 1 7 8 9 

def recur(index, curr):
    if index == m:
        answer.append(curr)
        return
    
    for i in nums:
        if len(curr) != 0:
            if i in curr or curr[-1] > i:
                continue
        curr.append(i)
        recur(index+1, curr[:])
        curr.pop()

answer = []    
recur(0, [])
for a in answer:
    print(*a)