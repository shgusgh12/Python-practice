#가능하면 최대한 많이 나누는 작업부터 진행하여 최적의해 보장한다

n, k = map(int, input().split()) 
cnt = 0
while True:
    #n이 k로 나누어 떨어지는 수가 될때까지 빼기
    target = (n // k) * k
    cnt += (n-target)
    n = target
    #n이 k보다 작을때 반복문 탈출
    if n < k:
        break
    #k로 나누기
    cnt += 1
    n //= k

cnt += (n-1)
print(cnt) 
    
    
