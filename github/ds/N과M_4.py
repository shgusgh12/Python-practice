import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [i for i in range(1,n+1)]

def func(nums, curr=[]):
    ans = []
    def backtracking(curr):
        if len(curr) == m:
            ans.append(curr)
            return 

        for i in range(1,n+1):
            if len(curr) >= 1 and curr[-1] > i:
                continue
            curr.append(i)
            backtracking(curr[:])
            curr.pop()
    backtracking([])
    return ans

answer = func(nums, curr=[])

for a in answer:
    print(*a)