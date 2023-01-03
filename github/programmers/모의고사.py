def solution(answers):
    answer = []
    arr1 = [1,2,3,4,5] * len(answers)
    arr2 = [2,1,2,3,2,4,2,5] * len(answers)
    arr3 = [3,3,1,1,2,2,4,4,5,5] * len(answers)

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(answers)):
        if arr1[i] == answers[i]:
            cnt1 += 1
        if arr2[i] == answers[i]:
            cnt2 += 1
        if arr3[i] == answers[i]:
            cnt3 += 1             
    ans = []        
    answer.append(cnt1)
    answer.append(cnt2)
    answer.append(cnt3)
    large = max(answer)
    cnt = 0
    idx = 0
    for i in range(3):
        if large == answer[i]:
            ans.append(i+1)

    ans.sort()
    return ans
