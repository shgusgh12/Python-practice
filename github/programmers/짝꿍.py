#join 함수 사용

def solution(X, Y):
    answer = ''
    xnum = {str(i): 0 for i in range(10)}
    ynum = {str(j): 0 for j in range(10)}
    for i in X:
        if i in xnum:
            xnum[i] += 1
    for i in Y:
        if i in ynum:
            ynum[i] += 1
    
    for k in range(9,-1,-1):
        k = str(k)
        less = min(xnum[k], ynum[k])
        
        if answer == '' and k == '0' and less != 0:
            return '0'
        
        #'9' * 3 = '999'되는 방식 사용함
        #''.join 함수 문자열을 연결해주는 함수 [a,b,c] => 'abc'
        answer = ''.join([answer,k*less])
    
    if answer == '':
        return '-1'
    else:
        return answer
    
        
    
