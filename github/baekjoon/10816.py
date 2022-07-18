N = int(input())
cards = list(map(int, input().split(' ')))
M = int(input())
t = list(map(int, input().split(' ')))
cards.sort

def binsearch(target):
    low = 0
    high = N-1
    mid = (low + high)//2
    while low <= high:
        if cards[mid] == target:
            return mid
        elif cards[mid] < target:
            high = mid - 1
        else:
            low = mid + 1
arr = [] 
cnt = 0
for i in range(M):
    if binsearch(t[i]) > 0:
        cnt += 1
        arr[i] = cnt
    

