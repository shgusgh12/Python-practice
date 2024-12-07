import sys

input = sys.stdin.readline

n = int(input())

taste = [list(map(int, input().split())) for _ in range(n)]

def recur(idx, sour, bitter, use):
    global answer
    if idx == n:
        if use == 0:
            return
        result = abs(sour - bitter)
        answer = min(answer, result)
        return 

    #요리를 선택하는 경우
    recur(idx+1, sour * taste[idx][0], bitter+ taste[idx][1], use+1)
    #선택하지 않는 경우
    recur(idx+1, sour, bitter, use)


answer = 99999999999

recur(0,1,0, 0)

print(answer)