#문자열 개수를 딕셔너리로 표현하기

def solution(X, Y):
    arr = ''
    cnt = 0
    answer = ''
    for i in X:
        if i in Y:
            answer += i
            X.replace(i, '')
            Y.replace(i, '')
    if answer == '':
        arr = '-1'
    else:
        answer = list(answer)
        answer.sort(reverse=True)
        for i in range(len(answer)):
            arr += str(answer[i])
            
            
    
    return arr
