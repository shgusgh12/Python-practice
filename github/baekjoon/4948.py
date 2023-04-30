import sys
input = sys.stdin.readline

 


while True:
    n = int(input())
    answer = 0
    arr = [0] * (2*n+1)
    if n == 0:
        break

    for i in range(2, 2*n+1):
        if arr[i] == 0:
            for j in range(2*i,2*n+1,+i):
                arr[j] = 1

    for k in range(n+1,2*n+1):
        if arr[k] == 0:
            answer += 1

    print(answer)
    