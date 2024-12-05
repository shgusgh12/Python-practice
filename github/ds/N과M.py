import sys
input = sys.stdin.readline
# 4 2
n, m = map(int, input().split())
# 1 2 3 4 
list = [i for i in range(1, n+1)]

def func(nums, k):
    result = []

    def backtracking(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        # 오름차순으로 값을 배열에 넣는다 -> 원하던 길이가 맞는지 확인 -> 맞으면 pop 아니면 그 배열로 backtrack
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtracking(i+1,curr)
            curr.pop()
        
    backtracking(start=0, curr=[])
    return result

answer = func(list, m)

for ans in answer:
    print(*ans)

