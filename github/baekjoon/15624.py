import sys

n = int(sys.stdin.readline())
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    arr = []
    arr.append(0)
    arr.append(1)

    for i in range(2, n+1):
        b = arr.pop()
        a = arr.pop()
        arr.append(b)
        arr.append((b+a) % 1000000007)
    return arr.pop()
print(fibo(n))

    

