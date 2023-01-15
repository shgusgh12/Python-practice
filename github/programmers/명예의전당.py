def solution(k, score):
    arr = []
    answer = []
    for i in range(len(score)):
        if len(arr) < k:
            arr.append(score[i])
            arr.sort(reverse=True)
            answer.append(arr[-1])
        else:
            if min(arr) < score[i]:
                arr[-1] = score[i]
                arr.sort(reverse=True)
                answer.append(arr[-1])
            else:
                arr.sort(reverse=True)
                answer.append(arr[-1])
    
    
    
    return answer
