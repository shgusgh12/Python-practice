t = int(input())

def fibo(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fibo(k-1) + fibo(k-2)

for i in range(t):
    n = int(input())
    a = 0
    b=0
    if fibo(n) == 0:
        a +=1
    else:
        b+=1
    print(a , b)

