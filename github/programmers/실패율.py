def solution(N, stages):
    user = len(stages)
    answer = []
    ans = []
    old = 0
    for i in range(1,N+1):
        cnt = 0
        for j in range(len(stages)):
            if stages[j] == i:
                 cnt+=1
        if cnt == 0:
            answer.append(0)
        else:
            percent = cnt / user
            answer.append(percent)
        user -= cnt
    ans = sorted(answer, reverse=True)
    answer1 = [] 
    for i in range(len(ans)):
        #index 함수 => 그 자리에 맞는 index 변환해줌
        answer1.append(answer.index(ans[i])+1)
        answer[answer.index(ans[i])] =2   #실패율을 2로 변경해서 중복으로 걸리지 않게 하기
    
            
        
    return answer1
