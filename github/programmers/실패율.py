def solution(N, stages):
    user = len(stages)
    answer = []
    ans = []
    sta = [0 for _ in range(N+2)] 
    cnt1 = 0
    
    for j in range(user):
        for k in range(1,N+2):
            if stages[j] == k:
                sta[k] += 1
    old = 0
    for i in range(1,N+1):
        old = sta[i]
        percent = sta[i] / user
        answer.append(percent)
        user -= old
    #인덱스로 바꾸는 법
        
    
    return answer
