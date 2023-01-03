#수정필요
#에라토스테네스의 체

def solution(nums):
    even= []
    odd = []
    sum = []
    ans = []
    
    for i in range(len(nums)):
        if nums[i] % 2 != 0:
            odd.append(nums[i])
        else:
            even.append(nums[i])
            
    for i in range(len(even)):
        for j in range(len(even)):
            if i != j:
                sum.append(even[i] + even[j])
    for i in range(len(sum)):
        for j in range(len(odd)):
            ans.append(sum[i]+odd[j])
    cnt = 0
    arr = [True for i in range(len(ans)+1)]
    m = int(math.sqrt(len(ans))) + 1

    return answer
