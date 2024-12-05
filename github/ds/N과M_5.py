import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
def func():
    ans = []
    def backtracking(curr):
        if len(curr) == m:
            ans.append(curr)
            return 


        for i in range(len(nums)):
            if nums[i] in curr:
                continue
            curr.append(nums[i])
            backtracking(curr[:])
            curr.pop()
    backtracking([])

    return ans

answer =  func()

for a in answer:
    print(*a)