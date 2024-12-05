import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
visited = [False] * n

def backtracking(curr):
    if len(curr) == m:
        print(*curr)
        return
    
    curr_index = 0
    for i in range(n):
        if not visited[i] and curr_index != nums[i]:
            visited[i] = True
            curr.append(nums[i])
            curr_index = nums[i]
            backtracking(curr[:])
            visited[i] = False
            curr.pop()
    
backtracking([])

