def solution(dartResult):
    n =''
    answer = 0
    score = []
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n) **1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n) **3
            score.append(n)
            n = ''
        elif i == '*': 
            #-1 인덱스 활용하여 뒤에서부터 생각
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1
                
    answer += score[0] + score[1] + score[2]
    
    
    return answer
