def solution(nums):
    answer = 0
    take = len(nums)//2
    nums = set(nums)
    n = len(nums)
    arr = list(nums)
    if take >= len(arr):
        answer = len(arr)
    else:
        answer = take
      
    return answer
