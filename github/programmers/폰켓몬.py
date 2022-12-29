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


#간결하게 생각해보자
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
