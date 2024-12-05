import sys
input = sys.stdin.readline

n,m = map(int, input().split())

nums = list(map(int, input().split()))
answer = []
new = list(set(nums))
new.sort()
def recur(curr):
    if len(curr) == m:
        answer.append(curr)
        return
    
    for i in range(len(new)):
        if len(curr) != 0 and curr[-1] <= new[i]:
            curr.append(new[i])
        elif len(curr) == 0:
            curr.append(new[i])
        else:
            continue
        recur(curr[:])
        curr.pop()

recur([])

for a in answer:
    print(*a)
    