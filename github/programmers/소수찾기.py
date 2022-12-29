import math
#모든 True 는 소수
#에라토스테네스의 체 활용
def solution(n):
    answer = 0
    arr = [True for i in range(n+1)]
    m = int(math.sqrt(n)) + 1
    
    for i in range(2, m):
        if arr[i] == True:
            for j in range (2*i, n+1, i):
                arr[j] = False
    for i in range(n+1):
        if arr[i] == True:
            answer += 1
    answer -= 2
    return answer
