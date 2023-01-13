def solution(lottos, win_nums):
    answer = []
    ans = []
    lottos.sort()
    win_nums.sort()
    cnt = 0
    
    for i in lottos:
        if i == 0:
            cnt+=1
        for j in win_nums:
            if i == j:
                answer.append(j)
                
    total = len(answer) + cnt
    if total == 6:
        ans.append(1)
    elif total == 5:
        ans.append(2)
    elif total == 4:
        ans.append(3)
    elif total == 3:
        ans.append(4)
    elif total == 2:
        ans.append(5)
    else:
        ans.append(6)
        
    if len(answer) == 6:
        ans.append(1)
    elif len(answer) == 5:
        ans.append(2)
    elif len(answer) == 4:
        ans.append(3)
    elif len(answer) == 3:
        ans.append(4)
    elif len(answer) == 2:
        ans.append(5)
    else:
        ans.append(6)   
    
    return ans
