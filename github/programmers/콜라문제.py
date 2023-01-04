def solution(a, b, n):
    #빈병 a 콜라 b병 준다  n개의 콜라 가지고있음
    answer = 0
    while n >= a:
        #20 2(나머지)+6(몫) 2+2 1+1 
        div = n // a
        r = n % a
        answer += div
        n = r + div
        
        
    
    return answer
