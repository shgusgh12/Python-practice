#467
#max 함수는 문자열 이나 튜플 리스트에만 사용가능하다
T = int(input())
cnt = 0


for i in range(T):
    N, M  = map(int, input().split(' '))
    imp = list(map(int, input().split(' ')))
    idx = list(i for i in range(len(imp)))
    idx[M] = 'target'

    while True :
        if imp[0] == max(imp):
            cnt +=1 
            if 'target' == idx[0]:
                print(cnt)
                break
            else: 
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))