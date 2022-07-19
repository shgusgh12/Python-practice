

def binsearch(l, target, start, end):
    if start > end:
        return 0
    mid = (start + end) //2
    if l[mid] == target:
        return l[start:end+1].count(target)
    elif l[mid] > target:
        binsearch(l, target, start, mid-1)
    else:
        binsearch(l, target, mid+1, end)
N = int(input())
cards = list(map(int, input().split(' ')))
M = int(input())
t = list(map(int, input().split(' ')))


cnt = {} #hashing을 딕셔너리로 함

for i in cards:   #for문에서 i 값은 리스트의 첫번째 값을 의미한다 0이아님
    if i in cnt:
        cnt[i] += 1 #키값은 그대로 들어가고 value값증가한다 ex) 10:1 이런식
    else:
        cnt[i] = 1 

for i in t:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')