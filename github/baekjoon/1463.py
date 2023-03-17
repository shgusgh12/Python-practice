import sys

n = int(sys.stdin.readline())
answer = 0
while True:

    if n % 2 ==0: # 짝수 
        if n % 3 == 1:
            n = n -1 
            answer += 1
        else:
            n = n //2
            answer += 1
    else: #홀수 
        if n % 3 == 0:
            n = n//3
            answer+=1
        else:
            n = n - 1
            answer += 1
    
    if n == 1:
        break
print(answer)
    
