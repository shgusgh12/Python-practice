#수정필요
#에라토스테네스의 체

import math
def solution(nums):
    ans = []
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1 , len(nums)):
                ans.append(nums[i] + nums[j] + nums[k])
    maxid = max(ans)
    arr = [True] * (maxid + 1)
    m = int(math.sqrt(maxid)) + 1
    
    for i in range(2,m):
        if arr[i] == True:
            for j in range(2*i, maxid+1, i):
                arr[j] = False
    for j in range(len(ans)):
        if arr[ans[j]] == True:
            answer += 1
    

    return answer
