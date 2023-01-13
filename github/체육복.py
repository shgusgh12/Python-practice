def solution(n, lost, reserve):
    answer = 0
    #set의 차집합 이용하여 다른 요소 빼기
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    
    for i in set_reserve:
        #왼쪽요소부터 주고 다음 오른쪽 요소
        if i-1 in set_lost:
            set_lost.remove(i-1)
            #pop은 안된다 remove 사용하기
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
    return n-len(set_lost)
