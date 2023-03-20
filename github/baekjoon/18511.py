from itertools import product

n, k = map(int, input().split())
arr = list(map(str, input().split()))
length = len(str(n))

while True:
    temp = list(product(arr, repeat=length))  # repeat 수만큼 리스트에서 중복순열로 추출한다
    ex = []
    for i in temp:
        now=int(''.join(i))
        if now <= n:
            ex.append(now)
    if len(ex) >= 1:
        print(max(ex))
        break
    else:
        length -= 1