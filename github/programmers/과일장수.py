

def solution(k, m, score):
    answer = 0
    n = len(score)//m
    score.sort(reverse=True)
    for i in range(0, len(score), m):
        if i+m <= len(score):
            answer += score[m+i-1]
    answer = answer * m
    return answer
