def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i] == 1:
            continue
        cnt = food[i] // 2
        answer += cnt * str(i)
    answer += '0'
    for j in range(len(food)-1,0,-1):
        if food[j] == 1:
            continue
        cnt2 = food[j] // 2
        answer += cnt2 * str(j)
    return answer
