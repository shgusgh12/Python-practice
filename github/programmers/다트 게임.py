#isnumeric 함수 숫자인지 판단해주는 함수

def solution(dartResult):
    n =''
    score = []
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n) **1
            score.append(n)
            n = ''
    
    
    
    answer = 0
    return answer
