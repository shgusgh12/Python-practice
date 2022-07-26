from typing import Any, Sequence

def binsearch(a: Sequence, key: Any) -> int :
    pl = 0
    pr = len(a) -1
    while True:
        pc = (pl+pr) //2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc+1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input())
    x = [None] * num 

    for i in range(num):
        x[i] = int(input()) #배열의 개수를 미리 지정한경우 append 말고 = 을 사용해야함
    x1 = sorted(x)

    ky = int(input('검색할 값 입력'))

    idx = binsearch(x1, ky)

    if idx == -1:
        print('검색실패')
    else:
        print(idx)